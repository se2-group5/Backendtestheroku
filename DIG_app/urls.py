"""DIG_app URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from main.viewsets import UserViewSet
from main import views

router = routers.DefaultRouter()
router.register(r'businesses', views.BusinessView, 'business')
router.register(r'cities', views.CityView, 'city')
router.register(r'consults', views.ConsultView, 'consult')
router.register(r'reports', views.ReportView, 'report')
router.register(r'favorites', views.FavoriteView, 'favorite')
router.register(r'users', UserViewSet)



urlpatterns = [
    path('', include('main.urls')), # when anybody is in the page without anything else it points now to main.urls
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    #path( 'tinymce/', include('tinymce.urls') ),
]
