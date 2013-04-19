from django.conf.urls import *

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^dog/', include('dog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
