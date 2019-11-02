from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import User
from parse import DataParser
import json

def index(request, user_id):
    return HttpResponse("Hello")

@login_required
def home(request, user_id):
    return HttpResponse()

@login_required
def questionnaire(request, user_id, questionnaire_id): #request, questionnaire-id
    print(request)
    return HttpResponse("questions here")

@login_required
def questionnaire_responses(request, user_id, questionnaire_id): #request, questionnaire-id
    print(request)
    return HttpResponse("responses here")

def getUsers(request):
    parser = DataParser()
    parser.parseFile("Participant-attribute-data.csv", True)
    response = parser.getQuestions()
    for val in response:
        thing = json.loads(val)
        newU = User()
        newU.userID = thing['id']
        newU.gender = thing['gender']
        newU.age = thing['age']
        newU.diagnosis = thing['diagnosis']
        newU.income = thing['income']
        newU.education = thing['education']
        newU.ethnicity = thing['ethnicity']
        newU.password = thing['password']
        newU.email = thing['email']
        newU.save()

    return HttpResponse("okaaaaaaaaaaa!")
