from src.file_storage import saveAnswerPool, saveQuiz

def createQuiz():
        quiz_title = input("Enter quiz title: ")
        quiz = {
                "title": quiz_title,
                "questions": []
        }

        isAdding = True              
        while isAdding:
                print()
                questionInput = input("Enter question: ")
                correctAnswer = input("Enter correct answer: ")
                question = {
                      "question": questionInput,
                      "answer": correctAnswer
                }
                quiz["questions"].append(question)
                print(quiz)
                saveAnswerPool(question["answer"], quiz["title"])
                # create choices pool for the newly created quiz, 
                # add the answer to the pool

                addQuestion = str(input("Do you want to add a question? (y/n): "))
                if addQuestion == "n" or addQuestion != "y": # TODO: refactor, redundant check if n
                      isAdding = False
        saveQuiz(quiz)

def editQuiz():
    print('edit quiz')

def deleteQuiz():
    print('delete quiz')