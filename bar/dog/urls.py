from django.conf.urls import patterns, url
from dog import views

print "in dog urls.py"
urlpatterns = patterns('', 
    url(r'^$', views.index, name='index')
)
print "end dog urls.py"
