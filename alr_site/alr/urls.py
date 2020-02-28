from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView

urlpatterns = [

    # public URLs
    url(r'^$', views.redirect_home, name='redirect_home'),
    url(r'^home/$', views.display_home, name='display_home'),
    url(r'^aboutUs/$', views.display_aboutUs, name='display_about'),
    url(r'^signUp/$', views.display_signUp, name='display_signUp'),

    # logged in users URLs
    url(r'^home/settings$', views.display_settings, name='display_settings'),

    # researcher URLs
    url(r'^viewData/$', views.display_viewData, name='display_viewData'),
    url(r'^uploadAudio/$', views.display_uploadAudio, name='display_uploadAudio'),
    url(r'^userManagement/$', views.display_userManagement, name='display_userManagement'),
    url(r'^trimAudio/$', views.display_trimAudio, name='display_trimAudio'),
    url(r'^createEval/$', views.display_createEval, name='display_createEval'),

    # evaluator URLs
    url(r'^rateData/$', views.display_rateData, name='display_rateData'),
    # for Evaluator login a simpler process
    url(r'^eval/login/$', views.display_evalLogin, name='display_evalLogin'),

    # For testing
    url(r'^taskBar/$', views.display_taskBar, name='display_taskBar'),


    # ajax URLs
    url(r'^ajax/createUser/$', views.ajax_createUser, name='ajax_createUser'),
    url(r'^ajax/loginUser/$', views.ajax_loginUser, name='ajax_loginUser'),
    url(r'^ajax/loginEvalUser/$', views.ajax_loginEvalUser, name='ajax_loginEvalUser'),

    url(r'^ajax/logoutUser/$', views.ajax_logoutUser, name='ajax_logoutUser'),

    url(r'^ajax/getAllAudioTrim/$', views.ajax_getAllAudioTrims, name='ajax_getAllAudioTrims'),


    url(r'^ajax/postRating/$', views.ajax_postRating, name='ajax_postRating'),
    url(r'^ajax/postUploadAudio/$', views.ajax_postUploadAudio, name='ajax_postUploadAudio'),
    url(r'^ajax/createEval/$', views.ajax_createEval, name='ajax_createEval'),

    # url(r'^ajax/registerUser/$', views.ajax_CreateUser, name='display_create_user'),

    #url(r'^test/$', views.display_test, name='test'),
    #url(r'^db_data/$', views.db_data, name='db_data'),


    # url(r'^test/$', views.display_test, name='test'),
    # url(r'^db_data/$', views.db_data, name='db_data'),
]
