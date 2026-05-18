from src.file_storage import loadQuizzes

def displayQuizzes(data):
        if not data:
                print("===== No quizzes yet! =====")
                return
        
        print("===== Quizzes =====")
        for index, quiz in enumerate(data):
                print(f"{index} - {quiz["title"]}")
        print("===================")

def answerQuiz(qna):
        for index, item in enumerate(qna):
                print(f"{index}. {item["question"]}")
                answer = input("answer - ")

def takeQuiz():
        data = loadQuizzes()
        # list and display quizes
        # choose which quiz to take
        displayQuizzes(data)
        quizIndex = int(input("Enter quiz: "))
        print(f"Taking quiz... {data[quizIndex]["title"]}")
        # 2 seconds delay
        answerQuiz(data[quizIndex]["questions"])