from django.conf.urls import url
from . import views


urlpatterns = [
	#url(r'^data/(?P<nodeid>\d+)/(?P<temp>\d+\.\d+)/(?P<humi>\d+\.\d+)/(?P<key>\d+)/$', views.getdata, name='getdata'),
	url(r'^data/(?P<nodeid>\d+)/(?P<temp>\d+\.\d+)/(?P<humi>\d+\.\d+)/(?P<key>\d+)/?$', views.getdata, name='getdata'),
	url(r'^getprogram/', views.getprogram, name='getprogram'),
	url(r'^gensn/', views.genSN, name='gensn'),

]