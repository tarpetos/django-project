"""password_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

# from users import views as user_views
from users.views import users_views
from users.views import usage_views
from users.views import countries_views

urlpatterns = [
    path('', users_views.users_list, name='home'),
    path('usage/', usage_views.usage_table, name='usage'),
    path('countries/', countries_views.countries_list, name='countries'),

    path('users/add', users_views.users_add, name='users_add'),
    path('users/<int:uid>/edit', users_views.users_edit, name='users_edit'),
    path('users/<int:uid>/usage', users_views.users_usage, name='users_usage'),
    path('users/<int:uid>/delete', users_views.users_delete, name='users_delete'),

    path('countries/add', countries_views.countries_add, name='countries_add'),
    path('countries/<int:cid>/edit', countries_views.countries_edit, name='countries_edit'),
    path('countries/<int:cid>/usage', countries_views.countries_usage, name='countries_usage'),
    path('countries/<int:cid>/delete', countries_views.countries_delete, name='countries_delete'),

    path('admin/', admin.site.urls),
]
