import random
import os
import sys
import time
from highscores import showHighscore, saveHighscore
from numcheck import checkDivisible, checkEven, checkPrime


def checkGuess(userInput, numTries, randomNumber):
    if (int(userInput) == randomNumber):
        print("Your guess was right!")
        numTries += 1
        print("Generating new number.\n")

    elif (int(userInput) > randomNumber):
        print("The number is smaller!")
        numTries += 1

    elif (int(userInput) < randomNumber):
        print("The number is bigger!")
        numTries += 1


def restart_game(maxNumber):
    print('\n Starting new game.')
    randnumber = random.randint(0, maxNumber)

    for i in [3, 2, 1]:
        print('{}\n' .format(i))
        time.sleep(1)

    return randnumber


def surrender(random_num, numTries):
    print("The number was: " + str(random_num))
    print("The number of your tries: " + str(numTries))
    print('\nGenerating new number')


def main():
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
    numTries = 0

    # Initialising starting screen
    os.system('clear')
    print("Welcome in the GuessTheNumber game, where You have to guess the generated number (0 <= X < 100) to WIN")
    print("\n      ¯\(°_o)/¯\n")
    userName = input("Please enter your name: ") or "Unkown soldier"
    difficulty = input(
        "Enter difficulty level: noob - medium - hard: ").lower()
    diff_dictionary = {'noob': 10, 'medium': 50, 'hard': 200}
    randomNumber = restart_game(diff_dictionary[difficulty])

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

            elif (userInput == ("even" or "odd")):
                checkEven(randomNumber)
                numTries += 1

            elif (userInput == 'divisible'):
                checkDivisible(int(input("Enter the divider: ")), randomNumber)
                numTries += 1

            # Surrender
            elif (userInput == "surrender"):
                surrender(randomNumber, numTries)
                randomNumber = restart_game(diff_dictionary[difficulty])

            # ShowHighscore
            elif (userInput == "highscore"):
                showHighscore()

            # Exit
            elif (userInput == "exit"):
                print("Goodbye!")
                quit()

            else:
                print("          Enter a number or an available command!\n")
        else:
            try:
                int(userInput)
                if (checkGuess(userInput, numTries, randomNumber) == 1):
                    saveHighscore(highscoreList, userName,
                                  numTries, difficulty)
            except ValueError:
                print("          Enter a number or an available command!\n")


if __name__ == "__main__":
    main()
