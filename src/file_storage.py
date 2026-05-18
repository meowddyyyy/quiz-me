import json

quizFile = "database/quizzes.json"

# check if file exist
# create file if not
def loadQuizzes():
        with open(quizFile, "r") as file:
                return json.load(file)

def saveQuiz(quiz):
        data = loadQuizzes()
        data.append(quiz)
        # get existing file content
        # merge or add the quiz
        # then save the updated content
        with open(quizFile, "w") as file:
                json.dump(data, file, indent=8)