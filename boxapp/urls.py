from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^add/?$', views.add_box, name='add_box'),
	    # url(r'^accounts/?$', views.accounts.AccountListView.as_view(), name='account_list'),

]