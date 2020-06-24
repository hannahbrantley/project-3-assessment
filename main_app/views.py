from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Item

# Create your views here.
def home(request):
  items = Items.objects.all()
  return render(request, 'index.html', { 'items': items })

class ItemList(ListView):
    model = Item

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'

class ItemDelete(DeleteView):
    model = Item
    success_url = '/'


