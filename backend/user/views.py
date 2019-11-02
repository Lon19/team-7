from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import User
from parse import DataParser
import json

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

def getUsers(request):
    parser = DataParser()
    parser.parseFile("Participant-attribute-data.csv", True)
    response = parser.getResponses()
    for val in response:
        newU = User()
        newU.userID = val[0]
        newU.gender = val[1]
        newU.age = val[2]
        newU.diagnosis = val[3]
        newU.income = val[4]
        newU.education = val[5]
        newU.ethnicity = val[6]
        newU.password = val[7]
        newU.email = val[8]
        newU.save()

    return HttpResponse("okaaaaaaaaaaa!")

def researcher_home(request, user_id):
    return HttpResponse()

def researcher_questionnaire_data(request, user_id, params):
    return HttpResponse()
