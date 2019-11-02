from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def index(request, user_id):
    return HttpResponse("Hello")

def user_home(request, user_id):
    return HttpResponse()

def user_questionnaire(request, user_id, questionnaire_id): #request, questionnaire-id
    print(request)
    return HttpResponse("questions here")

def user_questionnaire_responses(request, user_id, questionnaire_id): #request, questionnaire-id
    print(request)
    return HttpResponse("responses here")

def researcher_home(request, user_id):
    return HttpResponse()

def researcher_questionnaire_data(request, user_id, params):
    return HttpResponse()