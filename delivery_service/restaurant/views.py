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

class RestaurantCreateView(RestaurantFormMixin, CreateView):
    template_name = 'restaurant/restaurant_create.html'

class RestaurantUpdateView(RestaurantFormMixin, UpdateView):
    template_name = 'restaurant/restaurant_create.html'

class RestaurantDeleteView(RestaurantFormMixin, DeleteView):
    template_name = 'restaurant/restaurant_create.html'

