from django.forms import inlineformset_factory
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from .filters import Orderfilter
# Create your views here.
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

def products(request):
    products = Product.objects.all()
    
    context = {
        'product' : products
    }
        
    return render (request,'accounts/products.html',context)


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
    return render(request,'accounts/order_form.html',context)

def delete_order(request,pk):
    order = Order.objects.get(id = pk)
    context = {
            'item':order
    }
    if request.method == 'POST':
        order.delete()
        return redirect('home')
    return render(request,'accounts/delete_order.html',context)