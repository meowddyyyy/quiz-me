from src.quiz_management import createQuiz, editQuiz, deleteQuiz
from src.quiz_taking import takeQuiz

# config
running = True

def displayMenu():
        menu = f'\n| ====== MENU ====== |\n| 1 - Take a quiz    |\n| 2 - Create a quiz  |\n| 3 - Edit a quiz    |\n| 4 - Delete a quiz  |\n| 5 - Exit           |\n| ================== |\n'
        print(menu)

def exit():
        print('exiting...')
        global running
        running = False

menu_actions = {  # dictionary mapping
        "1": takeQuiz,      # value is the reference to the function
        "2": createQuiz,
        "3": editQuiz,
        "4": deleteQuiz,
        "5": exit
}

while running:
        displayMenu()

        option = input("Enter option: ")
        action = menu_actions.get(option) # gets the method

        if action:
             action() # executes the method that  we took
        else:
             print('Invalid option!')


# TODOS:
        # add time delay for inputs