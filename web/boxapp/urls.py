from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^add/?$', views.add_box, name='add_box'),
	url(r'^mybox/?$', views.mybox, name='mybox'),
	url(r'^box/(?P<pk>[0-9]+)/change?$', views.UpdateBoxView.as_view(), name='update_box'),
	url(r'^buyproduct/?$', views.buy_box, name='buy_box'),
	url(r'^buy/success/?$', views.buybox_success, name='buybox_success'),
	url(r'^contact/?$', views.contact, name='contact'),
	url(r'^detail/(?P<pk>[0-9]+)/?$', views.detail_box, name='detail_box'),
	url(r'^buyproduct/?$', views.buybox, name='buybox'),
	url(r'^contact/?$', views.contact, name='contact'),
	url(r'^add/profile/(?P<pk>\d+)/?$', views.add_box_profile, name='add_box_profile'),
	url(r'^delete/(?P<pk>\d+)', views.delete_box, name='delete_box'),
	url(r'^payment/?$',views.model_form_upload,name='uploadPayment'),
	url(r'^buy/payment/?$',views.model_form_upload,name='uploadPayment'),
]
