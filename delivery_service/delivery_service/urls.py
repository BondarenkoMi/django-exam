"""
URL configuration for delivery_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.views.generic import CreateView
from django.contrib.auth import get_user_model

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls', namespace='restaurant')),
    path('dishes/', include('dish.urls', namespace='dish')),
    path('reviews/', include('review.urls', namespace='review')),
]

User = get_user_model()
auth_urls = [
    path(
        'login/',
        auth_views.LoginView.as_view(),
        name='login',
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(
            template_name='registration/logout.html'
        ),
        name='logout',
    ),
    path(
        'signup/',
        CreateView.as_view(
            form_class=UserCreationForm,
            success_url='/',
            template_name='registration/registration_form.html',
        ),
        name='registration'
    ),
    path(
        'change_password/<int:id>/',
        CreateView.as_view(
            form_class=SetPasswordForm(User),
            template_name='registration/password_change_form.html',
            success_url='/'
        ),
        name='password_change'
    )
]

urlpatterns += [path('auth/', include(auth_urls))]

