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
    url(r'^viewAudio/$', views.display_viewAudio, name='display_viewAudio'),
    url(r'^uploadAudio/$', views.display_uploadAudio, name='display_uploadAudio'),
    url(r'^shareAudio/$', views.display_shareAudio, name='display_shareAudio'),
    url(r'^trimAudio/$', views.display_trimAudio, name='display_trimAudio'),
    url(r'^createEval/$', views.display_createEval, name='display_createEval'),

    # evaluator URLs
    url(r'^rateAudio/$', views.display_rateAudio, name='display_rateAudio'),
    # for Evaluator login a simpler process
    url(r'^eval/login/$', views.display_evalLogin, name='display_evalLogin'),

    # For testing
    url(r'^taskBar/$', views.display_taskBar, name='display_taskBar'),
    url(r'^testview/$', views.display_test1, name='display_test1'),
    url(r'^testrate/$', views.display_test2, name='display_test2'),


    # ajax misc. URLs
    url(r'^ajax/createUser/$', views.ajax_createUser, name='ajax_createUser'),
    url(r'^ajax/loginUser/$', views.ajax_loginUser, name='ajax_loginUser'),
    url(r'^ajax/loginEvalUser/$', views.ajax_loginEvalUser, name='ajax_loginEvalUser'),

    url(r'^ajax/logoutUser/$', views.ajax_logoutUser, name='ajax_logoutUser'),
    url(r'^ajax/createEval/$', views.ajax_createEval, name='ajax_createEval'),

    # ajax get
    url(r'^ajax/getAllAudioTrims/$', views.ajax_getAllAudioTrims, name='ajax_getAllAudioTrims'),
    url(r'^ajax/getAllLanguages/$', views.ajax_getAllLanguages, name='ajax_getAllLanguages'),
    url(r'^ajax/getAudioFileById/$', views.ajax_getAudioFileById, name='ajax_getAudioFileById'),

    # ajax post
    url(r'^ajax/postUploadAudio/$', views.ajax_postUploadAudio, name='ajax_postUploadAudio'),
    url(r'^ajax/postRecordedAudio/$', views.ajax_postRecordedAudio, name='ajax_postRecordedAudio'),

    url(r'^ajax/postRating/$', views.ajax_postRating, name='ajax_postRating'),
    url(r'^ajax/postTrimAudio/$', views.ajax_postTrimAudio, name='ajax_postTrimAudio'),

    # url(r'^ajax/registerUser/$', views.ajax_CreateUser, name='display_create_user'),

    #url(r'^test/$', views.display_test, name='test'),
    #url(r'^db_data/$', views.db_data, name='db_data'),


    # url(r'^test/$', views.display_test, name='test'),
    # url(r'^db_data/$', views.db_data, name='db_data'),
]
