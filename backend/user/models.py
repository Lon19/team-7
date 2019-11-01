from django.db import models

file = "../../Sample Data/wpforms-Autistica-8211-Work-Self-Confidence-10-29-2019.csv"


class Questionnaire(models.Model):
    questionnaireID = models.IntegerField
    questionnaireName = models.CharField(max_length=200)

class QuestionnaireQuestion(models.Model):
    questionnaireID = models.ForeignKey(Questionnaire, on_delete=models.CASCADE) #check
    questionID = models.IntegerField
    questionType = models.IntegerField
    questionText = models.CharField(max_length=200)

class User(models.Model):
    userID = models.IntegerField
    gender = models.CharField(max_length)=20
    age = models.Char
