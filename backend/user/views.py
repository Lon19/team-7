from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from parse import DataParser
import json
import datetime


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
        val = json.loads(val)
        newU.userID = val['id']
        newU.gender = val['gender']
        newU.age = val['age']
        newU.diagnosis = val['diagnosis']
        newU.income = val['income']
        newU.education = val['education']
        newU.ethnicity = val['ethnicity']
        newU.password = val['password']
        newU.email = val['email']
        newU.save()

    return HttpResponse("okaaaaaaaaaaa!")

def getAnswers(request):
    parser = DataParser()
    parser.parseFile("wpforms-Autistica-8211-Work-Self-Confidence.csv", False)
    question = parser.getQuestions()
    # Create a questionnaire and questions
    quest = Questionnaire();
    quest.questionnaireName = question[0]
    quest.save()
    qArr = []
    for i in range(4,len(question)):
        qs = Question()
        qs.questionnaireID = quest
        qs.questionType = question[i][1]
        qs.questionText = question[i][0]
        qs.save()
        qArr.append(qs)
    response = parser.getResponses()
    print(len(response))
    for j in range(1,500):
        date = response[j][-2]
        userID = response[j][2]
        #print(response)
        print(j)
        for i in range(3,len(response[1])-2):
            ans = Answers()
            ans.questionID = qArr[i-3]
            ans.userID = userID
            ans.date = datetime.datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")
            done = False
            for k in range(len(AnswerType.objects.all())):
                aa = AnswerType.objects.all()[k]
                if aa.textRef == response[j][k]:
                    ans.answer = k
                    done = True
                    break
            if not done:
                ans.answer = 1
            ans.save()

    #print(response)
    return HttpResponse("kk")

def researcher_home(request, user_id):
    return HttpResponse()

def researcher_questionnaire_data(request, user_id, params):
    return HttpResponse()
