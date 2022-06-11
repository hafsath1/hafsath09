"""hack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from.import views
urlpatterns = [
    path('',views.display),
    path('display1',views.display1),
    path('display2',views.display2),
    path('display3',views.display3),
    path('display4',views.display4),
    path('display5',views.display5),
    path('display6',views.display7),
    path('display8',views.display8),
    path('display9',views.display9),
    path('display10',views.display10),
]
