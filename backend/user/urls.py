# user URL Configuration

from django.urls import path

from . import views

""" This urls file determines each of the path ends for the /user section,
    along with their views functions"""

urlpatterns = [
    path('', views.index, name='index'), # index pages
    path('users', views.getUsers, name='users'), # used to save users, should be automatic
    path('answers', views.getAnswers, name='answers'), # used to add answers, should also be automatic
    path('respondent/home', views.user_home, name='user_home'),
    path('respondent/<int:user_id>/questionnaire/<int:questionnaire_id>', views.user_questionnaire, name='questionnaire'),
    path('respondent/<int:user_id>/visualisation/<int:questionnaire_id>', views.user_questionnaire_responses, name='questionnaire-responses'),
    path('researcher/home', views.researcher_home, name="researcher_home"),
    path('researcher/<int:user_id>/visualisation/<int:questionnaire_id>', views.researcher_questionnaire_data, name='research_q_data'),
]
