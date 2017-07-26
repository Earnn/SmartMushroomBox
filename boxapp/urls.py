from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^add/?$', views.add_box, name='add_box'),
	url(r'^mybox/?$', views.mybox, name='mybox'),
	url(r'^buyproduct/?$', views.buybox, name='buybox'),
	url(r'^contact/?$', views.contact, name='contact'),
	url(r'^add/profile/(?P<pk>\d+)/?$', views.add_box_profile, name='add_box_profile'),
	url(r'^delete/(?P<pk>\d+)', views.delete_box, name='delete_box'),
]
