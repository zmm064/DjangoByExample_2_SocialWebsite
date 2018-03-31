from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #url(r'^login/$', views.user_login, name='login'),
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^register/$', views.register, name='register'),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout_then_login/$', auth_views.logout_then_login, name='logout_then_login'),

    url(r'^passowrd-change/$', auth_views.password_change, name='passowrd_change'),
    url(r'^password-change/done/$', auth_views.password_change_done, name='password_change_done'),


    url(r'^passowrd-reset/$', auth_views.password_reset, name='passowrd_reset'),
    url(r'^passowrd-reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^passowrd-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^passowrd-reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),


]
