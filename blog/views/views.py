from django.shortcuts import render
from django.core.paginator import Paginator
from ..forms import CustomerModelForm,ProductListModelForm

from blog.models import Product
from django.db.models import Q
from ..models import Customer
from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/index.html', context)


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    attributes = product.get_attributes()

    context = {
        'product': product,
        'attributes': attributes
    }
    return render(request, template_name='blog/product-detail.html', context=context)


def customers(request):
    customers = Customer.objects.all()
    paginator = Paginator(customers, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    search_query = request.GET.get('search')
    if search_query:
        page_obj= Customer.objects.filter(Q(name__icontains=search_query)|(Q(email__icontains = search_query)))
    else:
        customers = Customer.objects.all()
    context = {
        
        'page_obj': page_obj,
    }
    return render(request, 'blog/customers.html', context)


def add_customer(request):
    customers = Customer.objects.all()
    form = CustomerModelForm()
    if request.method == 'POST':
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')

    context = {
        'customers': customers,
        'form': form
    }
    return render(request, 'blog/add-customer.html', context)





def customers_detail(request, pk):
    customers = Customer.objects.get(id=pk)
    context = {
        'customers': customers
    }
    return render(request, 'blog/customer-details.html', context)


def delete_customer(request, pk):
    customer = Customer.objects.filter(id=pk).first()
    if customer:
        customer.delete()
        return redirect('customers')
    context = {
        'customer': customer

    }
    return render(request,'blog/customer_details.html', context)


def update_customer(request,pk):
    customer = Customer.objects.get(id = pk)
    form = CustomerModelForm(instance=customer)
    if request.method =='POST':
           form = CustomerModelForm(request.POST, request.FILES, instance=customer)
           if form.is_valid():
               form.save()
               return redirect('customers_detail', pk)
           
    context = {
        'form': form,
        'customer': customer
    }
    return render(request, 'blog/update-customer.html', context)
               
        
        
        
    
    

