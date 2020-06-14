"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.splash, name='splash'),
    path('login', views.login, name='login'),
    path('lisence2', views.lisence2, name='lisence2'),
    path('lisence', views.lisence, name='lisence'),
    path('home', views.index, name='index'),
    path('id2', views.id2, name='id2'),
    path('id', views.id, name='id'),
    path('Birth', views.Birth, name='birth'),
    path('Birth2', views.Birth2, name='Birth2'),
    path('Birth3', views.Birth3, name='Birth3'),
]
