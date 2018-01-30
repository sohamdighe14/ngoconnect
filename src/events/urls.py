"""ngoconn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.views import LoginView, LogoutView



from .views import (
    HomeView,
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView
)
    

urlpatterns = [
    url(r'^$', EventListView.as_view(), name='List'),
    url(r'^create/$', EventCreateView.as_view(), name='Create'),
    url(r'^(?P<slug>[\w.@+-]+)/$', EventDetailView.as_view(), name='Details'),
    url(r'^(?P<slug>[\w.@+-]+)/edit/$', EventUpdateView.as_view(), name='Edit')
]
