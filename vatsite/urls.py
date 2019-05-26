"""vatsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from User import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[
    path(r'admin', admin.site.urls),
    url(r'^$', views.homePageView),
    url(r'^Home', views.homePageView),
    url(r'^about-us', views.aboutPageView),
    url(r'^services', views.servicePageView),
    url(r'^VATtraining', views.trainingPageView),
    url(r'^contact-us', views.contactPageView),
    url(r'^contact_complete', views.completePageView),
    url(r'^info', views.infoPageView),
    url(r'^rules', views.rulesPageView),
    url(r'^VATlaw', views.lawPageView),
]

urlpatterns += staticfiles_urlpatterns()