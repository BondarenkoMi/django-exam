from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Dish
from .forms import DishForm

class DishFormMixin(View):
    model = Dish
    form_class = DishForm
    success_url = '/'

class DishListView(ListView):
    model = Dish
    template_name = 'dish/dish_list.html'
    context_object_name = 'dishes'
    paginate_by = 10

class DishDetailView(DetailView):
    model = Dish
    template_name = 'dish/dish_detail.html'
    context_object_name = 'dish'

class DishCreateView(DishFormMixin, CreateView):
    template_name = 'dish/dish_create.html'

class DishUpdateView(DishFormMixin, UpdateView):
    template_name = 'dish/dish_create.html'

class DishDeleteView(DishFormMixin, DeleteView):
    template_name = 'dish/dish_create.html'

