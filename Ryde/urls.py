from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
     #url(r'^$', 'Ryde.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),
    #url (r'^$', include('v0.urls')),
    url (r'^v0/', include('v0.urls')),
    url(r'^admin/', include(admin.site.urls)),
) 

urlpatterns += staticfiles_urlpatterns()
