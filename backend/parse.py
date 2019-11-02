import csv
import json

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


    def getQuestions(self):
        questionResponse = []

        if not self.isUsers:
            questionResponse.append(json.dumps({'FormName': self.questions[1]}))
            questionResponse.append(json.dumps({'username': self.questions[2]}))
            questionResponse.append(json.dumps({'iD': self.questions[-2]}))
            questionResponse.append(json.dumps({'date': self.questions[-1]}))

            for i in range(3,len(self.questions)-2):
                questionJSON = {}
                questionJSON['questionText'] = self.questions[i]
                questionJSON['questionType'] = 1 # Hard coded for now
                questionResponse.append(json.dumps(questionJSON))

        else:
            for record in self.responses:
                questionJSON = {}
                questionJSON['id'] = record[0]
                questionJSON['gender'] = record[1]
                questionJSON['age'] = record[2]
                questionJSON['diagnosis'] = record[3]
                questionJSON['income'] = record[4]
                questionJSON['education'] = record[5]
                questionJSON['ethnicity'] = record[6]
                questionJSON['password'] = record[7]
                questionJSON['email'] = record[8]
                questionResponse.append(json.dumps(questionJSON))

        return questionResponse

    def getResponses(self):
        return self.responses
