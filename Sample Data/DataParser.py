import csv

class DataParser():


    def __init__(self, fileName):
        self.responses = []
        self.questions = []
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
        return self.questions

    def getResponses(self):
        return self.responses


data = DataParser("wpforms-Autistica-8211-Mental-Health.csv")
print(data.getQuestions())
