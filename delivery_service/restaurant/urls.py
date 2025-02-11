from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.RestaurantListView.as_view(), name='list'),
    path('restaurant/<int:pk>/', views.RestaurantDetailView.as_view(), name='detail'),
    path('restaurant/create/', views.RestaurantCreateView.as_view(), name='create'),
    path('restaurant/<int:pk>/update/', views.RestaurantUpdateView.as_view(), name='update'),
    path('restaurant/<int:pk>/delete/', views.RestaurantDeleteView.as_view(), name='delete'),
]