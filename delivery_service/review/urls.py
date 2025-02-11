from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('', views.ReviewListView.as_view(), name='list'),
    path('review/<int:pk>/', views.ReviewDetailView.as_view(), name='detail'),
    path('review/create/', views.ReviewCreateView.as_view(), name='create'),
    path('review/<int:pk>/update/', views.ReviewUpdateView.as_view(), name='update'),
    path('review/<int:pk>/delete/', views.ReviewDeleteView.as_view(), name='delete'),
]