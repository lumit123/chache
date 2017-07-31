"""thirdweb URL Configuration

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
from django.conf.urls import url , include
from django.contrib import admin
from chache import views as chache_views
from django.contrib.auth import urls as auth_urls
from django.views.generic.base import RedirectView

from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^favicon.ico$',RedirectView.as_view(url=r'static/images/favicon.ico')),  
    #url(r'^accounts/', include(auth_urls, namespace='accounts')),
    url(r'^accounts/', include('allauth.urls')),
    #url(r'^$', TemplateView.as_view(template_name='signup.html')),
    url(r'^$', RedirectView.as_view(url=r'accounts/login/')),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),
    url(r'^admin/', admin.site.urls),
    url(r'^index.html$', chache_views.index, name = 'index'),
    url(r'^add/$', chache_views.add, name = 'add'),
    url(r'^add/(\d+)/(\d+)/$', chache_views.add2, name = 'add2'),

    #ajax url
    url(r'^ajax_list/$',chache_views.ajax_list, name = 'ajax-list'),
    url(r'^ajax_dict/$',chache_views.ajax_dict, name = 'ajax-dict'),

    url(r'^(.*)\.html$', chache_views.appviews, name = 'appviews'),
]
