from django.db import models

file = "../../Sample Data/wpforms-Autistica-8211-Work-Self-Confidence-10-29-2019.csv"


class Questionnaire(models.Model):
    questionnaireName = models.CharField(max_length=200)

class QuestionType(models.Model):
    #questionTypeID = models.IntegerField()
    questionTypeName = models.CharField(max_length=200)

class Question(models.Model):
    questionnaireID = models.ForeignKey(Questionnaire, on_delete=models.CASCADE) #check
    questionType = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    questionText = models.CharField(max_length=200)

class User(models.Model):
    userID = models.IntegerField(primary_key=True)
    gender = models.IntegerField()
    age = models.IntegerField()
    diagnosis = models.IntegerField()
    income = models.IntegerField()
    education = models.IntegerField()
    ethnicity = models.IntegerField()
    password = models.CharField(max_length=64)



class AnswerType(models.Model):
    answerTypeID= models.IntegerField(primary_key=true)
    questionTypeID= models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    textRef = models.CharField(max_length=100)
    progRef = models.IntegerField()

class Answers(models.Model):
    questionID=models.ForeignKey(Question, on_delete=models.CASCADE)
    userID=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateField()
    answer=models.IntegerField()
