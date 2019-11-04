import csv
import json
from user.models import QuestionType, AnswerType

""" DataParser class is an API created with the purpose of decyphering the CSV
    files given to us from WordPress, to then send to the webserver to add to the database"""

# Note: This was initially fully using JSON, however python was handling it weirdly,
# So there was a last minute switch to arrays, despite this being bad practice
class DataParser():

    def __init__(self):
        self.responses = []
        self.questions = []
        self.isUsers = False

    """ parseFile opens the requested CSV file to return the questions and
        their responses, storing them into the respective arrays """
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

    """ determineQType is a (fairly rough) algorithm designed to figure out if
        the question is multiple choice or not, and if so, what kind of question it is"""
    def determineQType(self, index):
        options = []
        for record in self.responses:
            value = record[index];
            if value not in options:
                options.append(value)
        options.sort()
        name = ""
        # There needs to be a check to see if there are "too many" options
        # If so, then it must be an open ended question.
        for item in options:
            name += item[:9]
        #print(name)
        counter = 0
        for item in QuestionType.objects.all():# QuestionType name, concat of 10 chars of each thing
            if item.questionTypeName == name:
                return counter
            counter += 1
        else:
            #print("Ok I'm here")
            qType = QuestionType(questionTypeName=name)
            qType.save()
            # Algorithm to add answer types. Could also be improved with
            # table.models.add(records)
            for item in options:
                aType = AnswerType(answerTypeID=len(AnswerType.objects.all())+1)
                aType.questionTypeID = qType
                aType.textRef = item
                aType.progRef = len(AnswerType.objects.all())+1
                aType.save()
            return counter

    """ getQuestions searches the first line of the CSV to get each of the
        questions in the questionnaire, determining their types initially.
        This is then all added to the database.
        This works differently if isUsers is True"""
    def getQuestions(self):
        questionResponse = []

        if not self.isUsers:
            # These values only work if each CSV is the same, which can't be guaranteed
            # So would ideally be dynamically checked in code
            questionResponse.append(json.dumps({'FormName': self.responses[0][0]}))
            questionResponse.append(json.dumps({'username': self.questions[2]}))
            questionResponse.append(json.dumps({'iD': self.questions[-2]}))
            questionResponse.append(json.dumps({'date': self.questions[-1]}))

            for i in range(3,len(self.questions)-2):
                questionJSON = []
                questionJSON.append(self.questions[i])
                questionJSON.append(self.determineQType(i))
                questionResponse.append(questionJSON)
        else:
            return # Don't need it for users, at least for hackathon
        return questionResponse

    """ getResponses searches each of the other lines of the CSV to create a list
        of responses, containing the ID, date and answers. Or in the users case,
        it simply returns each of the user information values"""
    def getResponses(self):
        responses = []
        if not self.isUsers:
            for record in self.responses:
                # Ended
                responses.append(record)
            return responses
        else:
            for record in self.responses:
                # Password values need to be hashed
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


# data = DataParser()
# data.parseFile("wpforms-Autistica-8211-Mental-Health.csv",False)
# data.getQuestions()
# This was test code, used to test away from the server
