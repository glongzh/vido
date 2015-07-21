from django.conf.urls import patterns, include, url
from django.contrib import admin
from vidown.views import index, submit

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vido.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^submit/', submit),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^django-rq/', include('django_rq.urls')),
)
