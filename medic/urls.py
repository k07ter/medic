from django.conf.urls import patterns, include, url
#from .models import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'medic.views.home', name='home'),
    url(r'^output$', 'medic.views.output', name='output'),
    url(r'^doctor/$', 'medic.views.doctor', name='doctor'),
    url(r'^patients/$', 'medic.views.patients', name='patients'),
    url(r'^doctor/add$', 'medic.views.new_doctor', name='new_doctor'),
    url(r'^tickets$', 'medic.views.tickets', name='tickets'),
    url(r'^report$', 'medic.views.rep_comm', name='rep_comm'),
    # url(r'^$', 'medic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
