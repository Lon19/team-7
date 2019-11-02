from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import User
from parse import DataParser
import json

def index(request, user_id):
    return HttpResponse("Hello")

def user_home(request, user_id):
    return HttpResponse()

def user_questionnaire(request, user_id, questionnaire_name): #request, questionnaire-id
    parser = DataParser()
    parser.parseFile("Sample Data/" + questionnaire_name + ".csv", False)
    response = parser.getQuestions()
    print(response)
    questions = []
    for val in response:
        if "questionText" in val:
            questions.append(val)
    
    return HttpResponse(questions)

def user_questionnaire_responses(request, user_id, questionnaire_name): #request, questionnaire-id
    parser = DataParser()
    parser.parseFile("Sample Data/" + questionnaire_name + ".csv", False)
    question = parser.getQuestions()
    #print(question)
    questions = []
    for val in question:
        if 'questionText' in val:
            val_dict = json.loads(val)
            #print(val_dict)
            questions.append(val_dict.get('questionText'))
    questions.append('date')
    
        
    #print(questions)
    
    response = parser.getResponses()
    responses = []
    for vals in response:
        vals = vals[2:8]
        if str(user_id) in vals:
            for i, val in enumerate(vals):
                if val == "Strongly disagree" or val == "Did not apply to me at all":
                    vals[i] = 1
                elif val == "Somewhat disagree" or val == "A little":
                    vals[i] = 2
                elif val == "Somewhat agree" or val == "Applied to me to some degree" or val == "Moderate":
                    vals[i] = 3
                elif val == "Strongly agree":
                    vals[i] = 4
            vals = vals[1:]
            responses.append(vals)

    ques_and_resp = [{'question': question, 'response': response} for question, response in zip(questions, responses)]
    return HttpResponse(ques_and_resp)

def researcher_home(request, user_id):
    return HttpResponse()

def researcher_questionnaire_data(request, user_id, params):
    return HttpResponse()

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