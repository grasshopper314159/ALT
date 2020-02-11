from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView

urlpatterns = [

    url(r'^$', views.redirect_home, name='redirect_home'),
    url(r'^home/$', views.display_home, name='display_home'),
    url(r'^AboutUs/$', views.display_aboutUs, name='display_about'),
    url(r'^SignUp/$', views.display_signUp, name='display_signUp'),
    url(r'^ViewData/$', views.display_viewData, name='display_viewData'),
    url(r'^TaskBar/$', views.display_taskBar, name='display_taskBar'),


    url(r'^ajax/createUser/$', views.ajax_createUser, name='ajax_createUser'),
    url(r'^ajax/loginUser/$', views.ajax_loginUser, name='ajax_loginUser'),
    url(r'^ajax/logoutUser/$', views.ajax_logoutUser, name='ajax_logoutUser'),

    url(r'^ajax/getAllAudioTrim/$', views.ajax_getAllAudioTrims, name='ajax_getAllAudioTrims'),
    # url(r'^ajax/getGamePlayer/$', views.ajax_getGamePlayer, name='ajax_getGamePlayer'),
    # url(r'^ajax/registerUser/$', views.ajax_CreateUser, name='display_create_user'),

    #url(r'^test/$', views.display_test, name='test'),
    #url(r'^db_data/$', views.db_data, name='db_data'),


    # url(r'^test/$', views.display_test, name='test'),
    # url(r'^db_data/$', views.db_data, name='db_data'),
]
