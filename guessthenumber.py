import os
import random
import sys
import time
from highscores import showHighscore, saveHighscore
from numcheck import checkDivisible, checkEven, checkPrime


def checkGuess(userInput, name, numTries):
    if (int(userInput) == randomNumber):
        print("Your guess was right!")
        numTries += 1
        print("Generating new number.\n")
        for i in [3, 2, 1]:
            print('{}\n' .format(i))
            time.sleep(1)

        saveHighscore(highscoreList, name, numTries)
        generateNewNumber()
        print('Done!\n Starting new game.')

        for i in [0, 1, 2]:
            print('.')
            time.sleep(1)
        os.system('clear')

    elif (int(userInput) > randomNumber):
        print("The number is smaller!")
        numTries += 1

    elif (int(userInput) < randomNumber):
        print("The number is bigger!")
        numTries += 1


def generateNewNumber():
    randnumber = random.randint(0, 100)
    return randnumber


def surrender(random_num, numTries):
    print("The number was: " + str(random_num))
    print("The number of your tries: " + str(numTries))
    print('\nGenerating new number')
    os.system("eject cdrom")  # easteregg


if __name__ == "__main__":

    # Checks is there  file named 'highscore.txt', if not it creates a new one.
    if(os.path.exists("highscore.txt")):
        print("", end="")
    else:
        my_file = (open("highscore.txt", mode='w'))
        my_file.close()

    # Declaring variables
    commandList = ["help", "surrender", "highscore", "exit"]
    questionList = ["prime", "even", "odd", "divisible"]
    highscoreList = list()
    randomNumber = generateNewNumber()
    numTries = 0

    # Initialising starting screen
    os.system('clear')
    print("Welcome in the GuessTheNumber game, where You have to guess the generated number (0 <= X < 100) to WIN")
    print("\n      ¯\(°_o)/¯\n")
    userName = input("Please enter your name: ") or "Unkown soldier"
    print(randomNumber)

    # Main loop
    while True:
        print("Available commands: help - highscore - surrender - exit")
        userInput = (input("\nEnter a your guess: ")).lower()
        os.system('clear')

        if userInput.isalpha():
            # Help
            if (userInput == "help"):
                print("Available helps: prime - even/odd - divisible\n")

            elif (userInput == 'prime'):
                checkPrime(randomNumber)
                numTries += 1

            elif (userInput == r'[even,odd]'):
                checkEven(randomNumber)
                numTries += 1

            elif (userInput == 'divisible'):
                checkDivisible(int(input("Enter the divider: ")), randomNumber)
                numTries += 1

            # Surrender
            elif (userInput == "surrender"):
                surrender(randomNumber, numTries)
                randomNumber = generateNewNumber()

            # ShowHighscore
            elif (userInput == "highscore"):
                showHighscore()

            # Exit
            elif (userInput == "exit"):
                print("Goodbye!")
                quit()

            else:
                print("Enter a number or an available command!")
        else:
            checkGuess(userInput, userName, numTries)
