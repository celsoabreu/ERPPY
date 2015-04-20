from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf.urls.defaults import *
from cacd.views import *

# models -> Views -> URLS -> Templates
# cacd.views import AboutView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'cacd.views.listacli'),
	url(r'^itemagenda/$', 'cacd.views.Itemagenda'),
	url(r'^cliente/$', 'cacd.views.adccliente'),
    url(r'^detalhe_cli/(?P<nr_cli>\d+)/$', 'cacd.views.Detalhe_cli'),
    url(r'^detalhe_item/(?P<nr_item>\d+)/$', 'cacd.views.Detalhe_item'),
    

#url(r'^about/$', AboutView.as_view()),
		
    # Examples:
    # url(r'^Diretorio/$', 'cacd.views.adic_itemagenda', name = 'adic_itemagenda'),
    # url(r'^$', 'cafp.views.home', name='home'),
    # url(r'^cafp/', include('cafp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
