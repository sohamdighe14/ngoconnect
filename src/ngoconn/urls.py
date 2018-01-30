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

from profiles.views import ProfileFollowToggle, RegisterView, activate_user_view
from events.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^details/', include('accounts.urls',namespace='accounts')),
    url(r'^events/', include('events.urls',namespace='events')),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    url(r'^profile-follow/$', ProfileFollowToggle.as_view(), name='follow'),
    url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
]

# if settings.DEBUG:
#     urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
#     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
