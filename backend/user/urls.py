# visualisations URL Configuration

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # index pages
<<<<<<< HEAD
    path('respondent/home', views.user_home, name='user_home'),
    path('respondent/<int:user_id>/questionnaire/<int:questionnaire_id>', views.user_questionnaire, name='questionnaire'),
    path('respondent/<int:user_id>/visualisation/<int:questionnaire_id>', views.user_questionnaire_responses, name='questionnaire-responses'),
    path('researcher/home', views.researcher_home, name="researcher_home")
    path('researcher/<int:user_id>/visualisation/<int:questionnaire_id>')
=======
    path('home', views.home, name='home'),
    path('questionnaire/<int:questionnaire_id>', views.questionnaire, name='questionnaire'),
    path('users', views.getUsers, name='users'),
    #path('visualisation/<int:questionnaire_id>', views.questionnaire_responses, name='questionnaire-responses'),
>>>>>>> aa67b9ba35e1095fd68a720141063845c5dad3d2
]
