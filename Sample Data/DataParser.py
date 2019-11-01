import csv
<<<<<<< Updated upstream
=======
import json
>>>>>>> Stashed changes

class DataParser():


<<<<<<< Updated upstream
    def __init__(self, fileName):
        self.responses = []
        self.questions = []
=======
    def __init__(self):
        self.responses = []
        self.questions = []
        self.isUsers = False


    def parseFile(self, fileName, isUsers):
        self.isUsers = isUsers
>>>>>>> Stashed changes
        with open(fileName,'rt')as f:
            data = csv.reader(f)
            count = 0
            for row in data:
                if count == 0:
                    self.questions = row
                else:
                    self.responses.append(row)
                count += 1
<<<<<<< Updated upstream

    def getQuestions(self):
        return self.questions
=======
                

    def getQuestions(self):
        questionResponse = []

        if isUsers:
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
            
        
        return questionResponse
>>>>>>> Stashed changes

    def getResponses(self):
        return self.responses


<<<<<<< Updated upstream
data = DataParser("wpforms-Autistica-8211-Mental-Health.csv")
=======
data = DataParser()
#data.parseFile("wpforms-Autistica-8211-Mental-Health.csv", False)
data.parseFile("Participant-attribute-data.csv", True)

>>>>>>> Stashed changes
print(data.getQuestions())
