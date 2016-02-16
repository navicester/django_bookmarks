from django.conf.urls import patterns, include, url
from bookmarks.views import *
from django.conf.urls.defaults import *
#from django.views.generic.simple import direct_to_template
from django.views.generic import TemplateView
from django.shortcuts import render

import os.path
site_media = os.path.join(
    os.path.dirname(__file__), 'site_media'
)
#site_media = "E:/PythonWeb/code/django_bookmarks/django_bookmarks/site_media"

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    # url(r'^django_bookmarks/', include('django_bookmarks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # (r'^bookmarks$', main_page),
    (r'^$', main_page),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':site_media}), 
#    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'site_media'}),    
    (r'^user/(\w+)/$', user_page),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),     
    (r'^register/$', register_page),
    (r'^register/success/$', TemplateView.as_view(template_name = 'registration/register_success.html' )),
    (r'^save/$', bookmark_save_page),
    (r'^tag/([^\s]+)/$', tag_page),
    (r'^tag/$', tag_cloud_page),
	(r'^search/$', search_page),
    
    # test
    (r'^index/left/$', index_left),
    (r'^dropdownmenu/$', dropdown_menu),    
)
