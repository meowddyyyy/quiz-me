import random
from src.file_storage import loadQuizzes, loadChoices

def displayQuizzes():
        data = loadQuizzes()
        if not data:
                print("===== No quizzes yet! =====")
                return
        
        print("===== Quizzes =====")
        for index, quiz in enumerate(data):
                print(f"{index} - {quiz["title"]}")
        print("===================")

def generateChoices(correctAnswer, quizTitle):
        choices = []
        choices.append(correctAnswer)

        pool = loadChoices(quizTitle)
        filteredPool = []
        for item in pool:
                if item != correctAnswer:
                        filteredPool.append(item)

        if len(filteredPool) < 3:
                randomChoices = random.sample(filteredPool, len(filteredPool))
        else:
                randomChoices = random.sample(filteredPool, 3)

        for choice in randomChoices:
                choices.append(choice)

        random.shuffle(choices)

        return choices

def answerQuiz(questions, quizTitle):
        score = 0
        temporaryQuiz = []
        for index, item in enumerate(questions):
                print("========================================")
                print(f"{index}. {item["question"]}")
                print(item)
                print("")

                correctAnswer = item["answer"]
                choices = generateChoices(correctAnswer, quizTitle)
                for index, choice in enumerate(choices):
                        print(f"{index}. {choice}")

                userAnswer = int(input("Your answer - "))
                if choices[userAnswer] == correctAnswer:
                        print("correct")
                        score += 1
                else:
                        temporaryQuiz.append(item)
                        print("wrong")

        result = {
                "score": score,
                "temporaryQuiz": temporaryQuiz
        }
        return result

def takeQuiz():
        data = loadQuizzes()
        displayQuizzes()

        quizIndex = int(input("Enter quiz: "))
        if quizIndex > len(data) - 1:
                print("Cancelled. Returning to menu...")
                return

        quiz = data[quizIndex]
        print(f"Taking quiz... {quiz["title"]}")
        # 2 seconds delay
        result = answerQuiz(data[quizIndex]["questions"], quiz["title"])
        print(result)
        # TODO: result display and choices