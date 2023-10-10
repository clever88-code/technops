from pdb import post_mortem
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib import auth
from django.shortcuts import render
from bd.models import Products
from django.views.generic import ListView, DetailView, CreateView, FormView

def index(request):
    name_query = post_mortem.objects.order_by('-pub_date')
    return render(request, 'shop/index.html', context={'data_name_query': name_query})

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'about/about.html')

def product(request):
    product = Products.objects.all()
    return render(request, 'main/product.html', {'product': product})


class OrdersView(FormView):
    template_name = 'orders.html'
    form_class = Orders
    success_url = "/product"

    def form_valid(self, form):
        if form.is_valid:
            form.save()

        return super().form_valid(form)

