from django.forms import inlineformset_factory
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from .filters import Orderfilter
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group


@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username, password = password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid Username or Password')
        
    context = {}
    return render(request,'accounts/login.html',context)

def logoutuser(request):
    logout(request)
    return redirect('loginpage')

@unauthenticated_user
def registerpage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            group = Group.objects.get(name = 'customer')
            user.groups.add(group)
            
            Customer.objects.create(user = user,)
            
            messages.success(request,'Account was Created for '+ username)
            return redirect('loginpage')
    context = {
        'form':form
    }
    
    return render(request,'accounts/register.html',context)

@login_required(login_url='loginpage')
@admin_only
def home(request):
    order = Order.objects.all()
    customer = Customer.objects.all()
    
    total_customer = customer.count()
    total_order = order.count()
    
    delivered = order.filter(stauts = 'Delivered').count()
    pending = order.filter(stauts = 'Pending').count() 
    
    context = {
        'order':order,
        'customer': customer,
        'total_order':total_order,
        'total_customer':total_customer,
        'delivered':delivered,
        'pending':pending  
    }
    return render (request,'accounts/dashboard.html',context)


@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    
    context = {
        'product' : products
    }
        
    return render (request,'accounts/products.html',context)

@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['customer'])
def customer(request,pk):
    customer = Customer.objects.get(id = pk)
    order = customer.order_set.all()
    total_order = order.count()
    myfilter = Orderfilter(request.GET,queryset = order)
    order = myfilter.qs
    
    context = {
        'customer':customer,
        'order':order,
        'total_order':total_order,
        'myfilter':myfilter
    }
    return render (request,'accounts/customer.html',context)

@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def create_order(request,pk):
    orderformset = inlineformset_factory(Customer,Order, fields=('product','stauts'))
    customer = Customer.objects.get(id = pk)
    formset = orderformset(queryset=Order.objects.none(),instance= customer)
    if request.method == 'POST':
        formset = orderformset(request.POST,instance = customer)    
        if formset.is_valid():
            formset.save()
            return redirect('home')
    context = {
        'formset':formset
    }
    return render(request,'accounts/order_form.html',context)

@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def update_order(request,pk):
    
    order = Order.objects.get(id =pk)
    form = Orderform(instance=order)
    if request.method == 'POST':
        form = Orderform(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect ('home')
    context= {
        'form':form
    }
    return render(request,'accounts/update_order.html',context)

@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def delete_order(request,pk):
    order = Order.objects.get(id = pk)
    context = {
            'item':order
    }
    if request.method == 'POST':
        order.delete()
        return redirect('home')
    return render(request,'accounts/delete_order.html',context)

@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['customer'])
def userpage(request):
    orders = request.user.customer.order_set.all()
    order = Order.objects.all()
    total_order = order.count()
    
    delivered = orders.filter(stauts = 'Delivered').count()
    pending = orders.filter(stauts = 'Pending').count() 
    
    context = {
        'orders':orders,
        'total_order':total_order,
        'pending':pending,
        'delivered':delivered
        }
    return render(request,'accounts/user.html',context)



@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['customer'])
def account_settings(request):
    customer = request.user.customer
    form = CustomerForm(instance= customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            
    context = {
        'form': form
    }
    return render(request,'accounts/account_settings.html',context)
    