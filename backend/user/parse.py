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
                questionJSON['questionType'] = determineQType(i) # Hard coded for now
                questionResponse.append(json.dumps(questionJSON))
        else:
            return # Don't need it for users


        return questionResponse

    def determineQType(self):
        return 1

    def getResponses(self):
        responses = []
        if not self.isUsers:
            for record in self.responses:
                # Only count from 3 to -3
                qJSON = {}
                for i in range(3, len(record)-3):
                    string = 'q'+str(i)
                    qJSON[string] = record[i]
                responses.append(json.dumps(qJSON))

            return # Stub
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
                responses.append(json.dumps(questionJSON))
        return responses
