from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Review
from .forms import ReviewForm

class ReviewFormMixin(View):
    model = Review
    form_class = ReviewForm
    success_url = '/'

class ReviewListView(ListView):
    model = Review
    template_name = 'review/review_list.html'
    context_object_name = 'reviews'
    paginate_by = 10

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review/review_detail.html'
    context_object_name = 'review'

class ReviewCreateView(ReviewFormMixin, CreateView):
    template_name = 'review/review_create.html'


class ReviewUpdateView(ReviewFormMixin, UpdateView):
    template_name = 'review/review_update.html'

class ReviewDeleteView(ReviewFormMixin, DeleteView):
    template_name = 'review/review_delete.html'

