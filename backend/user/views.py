from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from parse import DataParser
import json
import datetime

""" Views file defines each of the functions used by pages of the django website"""

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

""" getUsers uses the DataParser class to decypher the user data
    It then adds new records to the database"""
def getUsers(request):
    parser = DataParser()
    parser.parseFile("Participant-attribute-data.csv", True)
    response = parser.getResponses()
    # This should really be in the parser
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

    return HttpResponse("Users added!")

""" getAnsers uses the DataParser class to decyper the response data and adds it
    to the respective databases, including questions, response types, the questionnaire
    and the answers"""
def getAnswers(request):
    parser = DataParser()
    parser.parseFile("wpforms-Autistica-8211-Work-Self-Confidence.csv", False)
    # File name can be changed to any csv
    # Would be useful to have the file uploaded by user/admin?
    question = parser.getQuestions()
    # Create a questionnaire and questions

    """ This is the "algorithm" to upload the entire questionnaire.
        This is quite inefficient, takes ~10 minutes to do 2500 records """
    quest = Questionnaire();
    quest.questionnaireName = question[0]
    quest.save() # record.save() is inefficient, perhaps use update()
    """ Upon further research, table.members.add(record1, .. recordN)
        could be used for potentially huge speed improvements See:
        https://docs.djangoproject.com/en/2.2/topics/db/optimization/#insert-in-bulk"""
    qArr = []
    for i in range(4,len(question)):
        qs = Question()
        qs.questionnaireID = quest
        qs.questionType = question[i][1]
        qs.questionText = question[i][0]
        qs.save()
        qArr.append(qs)
    response = parser.getResponses()
    #print(len(response))
    for j in range(1,len(response)): # Breaks at 500, due to date error
        date = response[j][-2]
        userID = response[j][2]
        #print(response) Debugging tools
        #print(j)
        for i in range(3,len(response[1])-2):
            ans = Answers()
            ans.questionID = qArr[i-3]
            ans.userID = userID
            ans.date = datetime.datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")
            # Switches the date into a normal format, as not done by parser
            # Sorry, doesn't count for the 30th February, perhaps the feature will exist on the 32nd October :)
            done = False
            # The following loop is inefficient, and will get more inefficient as time goes on
            # As it only needs to check answerTypes for it's category
            for k in range(len(AnswerType.objects.all())):
                aa = AnswerType.objects.all()[k]
                if aa.textRef == response[j][k]:
                    ans.answer = k
                    done = True
                    break
            if not done: # This shouldn't ever run
                ans.answer = 1
            ans.save()

    #print(response)
    return HttpResponse("Data saved!")

def researcher_home(request, user_id):
    return HttpResponse()

def researcher_questionnaire_data(request, user_id, params):
    return HttpResponse()
