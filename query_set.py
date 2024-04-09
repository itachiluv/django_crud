
from accounts.models import *
c1 = Customer.objects.all()
print(c1)
# <QuerySet [<Customer: Luffy>, <Customer: Itachi>, <Customer: Sung>]>
print(c1.first())
# Luffy
c2 = Customer.objects.get(name = 'Luffy')
print(c2)
# Luffy
print(c2.email)
# luffy@gmail.com
print(c2.phone)
985632147
c3 = Customer.objects.get(id = 2)
print(c3)
# Itachi
print(c3.name)
# Itachi
print(c3.eamil)

print(c3.email)
# itachi@gmail.com
order_c1 = c1.order_set.all()

print(c1)
# <QuerySet [<Customer: Luffy>, <Customer: Itachi>, <Customer: Sung>]>
order = c2.order_set.all()
print(order)
# <QuerySet [<Order: Order object (1)>, <Order: Order object (4)>]>
order = Order.objects.all()
print(order.customer.name)

order = Order.objects.first()
print(order.customer.name)
# Luffy
order = Order.objects.last()
print(order.customer.name)
# Itachi
p1 = Product.objects.filter(category= 'Outdoor')
print(p1)
# <QuerySet [<Product: Football>, <Product: Devil Fruit>]>
p1.first()
# <Product: Football>
p1_first = p1.first()
print(p1_first)
# Football
order = p1_first.order_set.all()
print(order)
# <QuerySet [<Order: Order object (2)>, <Order: Order object (4)>]>
order = order.objects.first()

order = Order.objects.first()
print(order.product.name)
# Devil Fruit
print(order.product.category)
# Outdoor/
print(order.product.date_created)
# 2024-04-09 09:21:15.467646+00:00
print(order.product.date_created.date())
# 2024-04-09
print(order.product.date_created.strftime('%Y-%m%d'))
# 2024-0409
print(order.product.date_created.strftime('%d-%m-%Y'))
# 09-04-2024
p1 = Product.objects.all().order_by('id')
print(p1)
# <QuerySet [<Product: Football>, <Product: Devil Fruit>, <Product: Laptop>]>
p1 = Product.objects.all().order_by('-id')
print(p1)
# <QuerySet [<Product: Laptop>, <Product: Devil Fruit>, <Product: Football>]>
p2 = Product.objects.filter(tag_name = 'Sports')

print(p1)
# <QuerySet [<Product: Laptop>, <Product: Devil Fruit>, <Product: Football>]>
p2 = Product.objects.filter(tag_name = 'Sports')

# customer = customer.object.first()

customer = Customer.object.first()

customer = Customer.objects.first()
print(customer)
# Luffy
allorder = {}

for order in customer.order_set.all():
    if order.product.name in allorder:
            allorder[order.product.name] += 1
    else:
            allorder[order.product.name] = 1
print(allorder)

print(allorder)
{}
ballorder = customer.order_set.filter(product__name='Football').count()
print(allorder)
{}
print(ballorder)
1
