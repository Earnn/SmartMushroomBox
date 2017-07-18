from django.conf.urls import url
from . import views

from django.contrib.auth import views as auth_views



urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,{'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    # url(r'import_rule/', views.import_rule, name='import_rule'),
    # url(r'accountlist/', AccountListView.as_view()),
]
# url(r'^$', core_views.home, name='home'),
#     url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
#     url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
#     url(r'^signup/$', core_views.signup, name='signup'),
# {% url 'case_search' account_no %}