# visualisations URL Configuration

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # index pages
    path('home', views.user_home, name='user_home'),
    path('<int:user_id>/questionnaire/<str:questionnaire_name>', views.user_questionnaire, name='questionnaire'),
    path('<int:user_id>/visualisation/<str:questionnaire_name>', views.user_questionnaire_responses, name='questionnaire-responses'),
    path('users', views.getUsers, name='users'),
]
