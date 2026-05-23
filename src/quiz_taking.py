import random
from src.file_storage import loadQuizzes, loadChoices

def displayQuizzes(data):
        if not data:
                print("===== No quizzes yet! =====")
                return
        
        print("===== Quizzes =====")
        for index, quiz in enumerate(data):
                print(f"{index} - {quiz["title"]}")
        print("===================")

def answerQuiz(questions, quizTitle):
        score = 0
        for index, item in enumerate(questions):
                print("========================================")
                print(f"{index}. {item["question"]}")
                print("")
                # algorithm for picking random choices and adding the correct answer to the choices array
                # choices = [correct one, random one, random two, random three]
                # shuffle the choices so that the answer is not on the same order

                # get the correct answer
                # get wrong random choices from the pool
                # combine them into choices array
                # shuffle
                # display multiple choices
                choices = []
                correctAnswer = item["answer"]
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
                for index, choice in enumerate(choices):
                        print(f"{index}. {choice}")

                userAnswer = int(input("Your answer - "))
                if choices[userAnswer] == correctAnswer:
                        print("correct")
                        score += 1
                else:
                        print("wrong")

                # if answer is equal to the questions answer add 1 to the score
                # if not, add the question to a temporary quiz

def takeQuiz():
        data = loadQuizzes()
        # list and display quizes
        # choose which quiz to take
        displayQuizzes(data)
        quizIndex = int(input("Enter quiz: "))
        quiz = data[quizIndex]
        print(f"Taking quiz... {quiz["title"]}")
        # 2 seconds delay
        answerQuiz(data[quizIndex]["questions"], quiz["title"])