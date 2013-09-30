from django.conf.urls import patterns, include, url
from django.contrib import admin
from lru import urls
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
  	(r'^lru/', include(urls)),

)
