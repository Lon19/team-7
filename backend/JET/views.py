from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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
    if request.user.is_authenticated():
        if user_id == int(request.user.username):
            return HttpResponse("you can see this")
    return HttpResponse("nope")