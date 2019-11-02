# visualisations URL Configuration

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # index pages
    path('home', views.home, name='home'),
    path('questionnaire/<int:questionnaire_id>', views.questionnaire, name='questionnaire'),
    path('users', views.getUsers, name='users'),
    #path('visualisation/<int:questionnaire_id>', views.questionnaire_responses, name='questionnaire-responses'),
]
