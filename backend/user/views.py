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
        depression = []
        anxiety = []
        stress = []
        #this might be the worst code i've ever written, i am terribly sorry
        for i in range(len(responses)):
            day_dep = responses[i][2] + responses[i][4] + responses[i][9] + responses[i][15] + responses[i][16] + responses[i][20]
            day_dep = day_dep * 2
            depression.append(day_dep)
            day_anx = responses[i][1] + responses[i][3] + responses[i][6] + responses[i][8] + responses[i][14] + responses[i][18] + responses[i][19]
            day_anx = day_anx * 2
            anxiety.append(day_anx)
            day_str = responses[i][0] + responses[i][5] + responses[i][7] + responses[i][10] + responses[i][11] + responses[i][13] + responses[i][17]
            day_str = day_str * 2
            stress.append(day_str)

        list_of_dicts = []
        for i in range(len(responses)-1):
            i=i+1
            mental_health_dict = {}
            mental_health_dict["Day"] = i
            mental_health_dict["Depression"] = depression[i]
            mental_health_dict["Anxiety"] = anxiety[i]
            mental_health_dict["Stress"] = stress[i]
            list_of_dicts.append(mental_health_dict)


        
        return HttpResponse(list_of_dicts)
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