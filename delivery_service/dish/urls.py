from django.urls import path
from . import views

app_name = 'dish'

urlpatterns = [
    path('', views.DishListView.as_view(), name='dish_list'),
    path('dish/<int:pk>/', views.DishDetailView.as_view(), name='dish_detail'),
    path('dish/create/', views.DishCreateView.as_view(), name='dish_create'),
    path('dish/<int:pk>/update/', views.DishUpdateView.as_view(), name='dish_update'),
    path('dish/<int:pk>/delete/', views.DishDeleteView.as_view(), name='dish_delete'),

]