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
        if str(user_id) in vals:
            for i, val in enumerate(vals):
                if val == "Strongly disagree" or val == "Did not apply to me at all":
                    vals[i] = 0
                elif val == "Somewhat disagree" or val == "A little" or val == "Applied to me to some degree":
                    vals[i] = 1
                elif val == "Somewhat agree" or val == "Moderate" or val == "Applied to me to a considerable degree":
                    vals[i] = 2
                elif val == "Strongly agree" or val == "Applied to me very much":
                    vals[i] = 3
            vals = vals[3:len(vals)-2]
            responses.append(vals)

    if "Mental-Health" in questionnaire_name:

        #this might be the worst code i've ever written, i am terribly sorry
        depression = sum(responses[2]) / len(responses[2]) + sum(responses[4]) / len(responses[4]) + sum(responses[9]) / len(responses[9]) + sum(responses[15]) / len(responses[15]) + sum(responses[16]) / len(responses[16]) + sum(responses[20]) / len(responses[20])
        depression = depression * 2
        anxiety = sum(responses[1]) / len(responses[1]) + sum(responses[3]) / len(responses[3]) + sum(responses[8]) / len(responses[8]) + sum(responses[14]) / len(responses[14]) + sum(responses[18]) / len(responses[18]) + sum(responses[19]) / len(responses[19])
        anxiety = anxiety * 2
        stress = sum(responses[0]) / len(responses[0]) + sum(responses[5]) / len(responses[5]) + sum(responses[7]) / len(responses[7]) + sum(responses[10]) / len(responses[10]) + sum(responses[11]) / len(responses[11]) + sum(responses[13]) / len(responses[13]) + sum(responses[17]) / len(responses[17])
        stress = stress * 2

        mental_health_dict = {'Depression': depression, 'Anxiety': anxiety, 'Stress': stress}
        mental_health_json = json.dumps(mental_health_dict)
        return HttpResponse(mental_health_json)
    else:
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