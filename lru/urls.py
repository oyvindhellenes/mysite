from django.conf.urls import patterns, url
from lru import views

urlpatterns = patterns('lru',
    url(r'^$', views.index),
	url(r'^create/$', views.create),
	
	url(r'^login/$', views.login),
	url(r'^auth/$', views.auth_view),
	url(r'^logout/$', views.logout),
	url(r'^loggedin/$', views.loggedin),
	url(r'^invalid/$', views.invalid_login),	
	url(r'^reservation/$', views.reservation),
)