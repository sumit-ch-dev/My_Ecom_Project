from django.shortcuts import render

# Import Views
from django.views.generic import ListView, DetailView

#models
from App_Shop.models import Product

# Create your views here.

class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'