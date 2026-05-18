from src.file_storage import loadQuizzes, saveQuiz

def createQuiz():
        quiz_title = input("Enter quiz title: ")
        quiz = {
                "title": quiz_title,
                "questions": []
        }

        isAdding = True              
        while isAdding:
                questionInput = input("Enter question: ")
                correctAnswer = input("Enter correct answer: ")
                question = {
                      "question": questionInput,
                      "answer": correctAnswer
                }
                quiz["questions"].append(question)
                print(quiz)

                addQuestion = str(input("Do you want to add a question? (y/n): "))
                if addQuestion == "n" or addQuestion != "y":
                      isAdding = False
        saveQuiz(quiz)

def editQuiz():
    print('edit quiz')

def deleteQuiz():
    print('delete quiz')