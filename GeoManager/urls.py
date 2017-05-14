"""GeoManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from GeoRiddles.views import (AddMystery, BaseView, DetailMystery, MysteryView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'geomanager$', BaseView.as_view(), name = 'base'),
    url(r'geomanager/mystery$', MysteryView.as_view(), name = 'mystery'),
    url(r'geomanager/mystery_detail/(?P<id>(\d)+)', DetailMystery.as_view(), name =  'mystery-detail'),
    url(r'geomanager/add_mystery', AddMystery.as_view(), name='add-mystery') 
]
