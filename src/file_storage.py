import json

quizFile = "database/quizzes.json"
choicesFile = "database/choices.json"

# check if file exist
# create file if not
def loadQuizzes():
        return loadFile(quizFile)

def saveQuiz(quiz):
        # get existing file content
        # merge or add the quiz
        # then save the updated content
        data = loadQuizzes()
        data.append(quiz)
        writeJsonFile(quizFile, data)

def saveAnswerPool(answer, title):
        data = loadFile(choicesFile)

        if title not in data:
                data[title] = []
        data[title].append(answer)

        writeJsonFile(choicesFile, data)

def loadChoices(quizTitle):
        data = loadFile(choicesFile)
        return data[quizTitle]

def loadFile(filedir):
        with open(filedir, "r") as file:
                return json.load(file)
        
def writeJsonFile(jsonFile, data):
        with open(jsonFile, "w") as file:
                json.dump(data, file, indent=8)