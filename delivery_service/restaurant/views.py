from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from .models import Restaurant
from .forms import RestaurantForm


class RestaurantFormMixin(View):
    model = Restaurant
    form_class = RestaurantForm
    success_url = '/'


class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant/restaurant_list.html'
    context_object_name = 'restaurants'
    paginate_by = 5

class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'restaurant/restaurant_detail.html'
    context_object_name = 'restaurant'

class RestaurantCreateView(CreateView, RestaurantFormMixin):
    template_name = 'restaurant/restaurant_create.html'

class RestaurantUpdateView(UpdateView, RestaurantFormMixin):
    template_name = 'restaurant/restaurant_create.html'

class RestaurantDeleteView(DeleteView, RestaurantFormMixin):
    template_name = 'restaurant/restaurant_create.html'

