import csv
import json
from user.models import QuestionType, AnswerType

class DataParser():


    def __init__(self):
        self.responses = []
        self.questions = []
        self.isUsers = False


    def parseFile(self, fileName, isUsers):
        self.isUsers = isUsers
        with open(fileName,'rt')as f:
            data = csv.reader(f)
            count = 0
            for row in data:
                if count == 0:
                    self.questions = row
                else:
                    self.responses.append(row)
                count += 1

    def determineQType(self, index):
        options = []
        for record in self.responses:
            value = record[index];
            if value not in options:
                options.append(value)
        options.sort()
        name = ""
        for item in options:
            name += item[:9]
        #print(name)
        counter = 0
        for item in QuestionType.objects.all():# QuestionType name, concat of 10 chars of each thing
            if item.questionTypeName == name:
                return counter
            counter += 1
        else:
            print("Ok I'm here")
            qType = QuestionType(questionTypeName=name)# TODO ADD ANSWER TYPES HERE
            qType.save()
            for item in options:
                aType = AnswerType(answerTypeID=len(AnswerType.objects.all())+1)
                aType.questionTypeID = qType
                aType.textRef = item
                aType.progRef = len(AnswerType.objects.all())+1
                aType.save()

            return counter

    def getQuestions(self):
        questionResponse = []

        if not self.isUsers:
            questionResponse.append(json.dumps({'FormName': self.responses[0][0]}))
            questionResponse.append(json.dumps({'username': self.questions[2]}))
            questionResponse.append(json.dumps({'iD': self.questions[-2]}))
            questionResponse.append(json.dumps({'date': self.questions[-1]}))

            for i in range(3,len(self.questions)-2):
                questionJSON = []
                questionJSON.append(self.questions[i])
                questionJSON.append(self.determineQType(i)) # Hard coded for now
                questionResponse.append(questionJSON)
        else:
            return # Don't need it for users


        return questionResponse


    def getResponses(self):
        responses = []
        if not self.isUsers:
            for record in self.responses:
                # Only count from 3 to -3
                responses.append(record)


            return responses
        else:
            for record in self.responses:
                questionJSON = []
                questionJSON.append(record[0])
                questionJSON.append(record[1])
                questionJSON.append(record[2])
                questionJSON.append(record[3])
                questionJSON.append(record[4])
                questionJSON.append(record[5])
                questionJSON.append(record[6])
                questionJSON.append(record[7])
                questionJSON.append(record[8])
                responses.append(questionJSON)
        return responses


data = DataParser()
data.parseFile("wpforms-Autistica-8211-Mental-Health.csv",False)
data.getQuestions()
