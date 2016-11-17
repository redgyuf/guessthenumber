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
        return 1

    elif (int(userInput) > randomNumber):
        print("The number is smaller!")
        numTries += 1

    elif (int(userInput) < randomNumber):
        print("The number is bigger!")
        numTries += 1


def restart_game(maxNumber):

    print('\nStarting new game.')
    randnumber = random.randint(0, maxNumber)

    for i in [5, 4, 3, 2, 1]:
        print('{}\n' .format(i))
        time.sleep(1)

    os.system('clear')

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

    highscoreList = list()
    numTries = 0

    # Initialising starting screen
    os.system('clear')
    print("Welcome in the GuessTheNumber game, where You have to guess the generated number to WIN")
    print("\n      ¯\(°_o)/¯\n")
    userName = input(
        "Please enter your name (max 16 characters): ") or "Unkown soldier"

    if len(userName) > len("Unknown soldier"):
        userName = "NemTudokOlvasni"

    os.system('clear')
    print("Hello Mr. {} :)" .format(userName))

    difficulty = input(
        "\nEnter difficulty level: noob - medium - hard - Versus Mode <vs>: ").lower()

    diff_dictionary = {'noob': 10, 'medium': 50,
                       'hard': 200, 'vs': 0}

    if (difficulty in diff_dictionary):
        pass
    else:
        os.system('clear')
        print("So you are too stupid to spell the difficulties, Difficulty set to NOOB!")
        difficulty = "noob"
        time.sleep(3)

    randomNumber = restart_game(diff_dictionary[difficulty])

    if diff_dictionary[difficulty] == 0:
        os.system('python3 aivsplayer.py')  # Start the AI vs Player program

    # Main loop
    # This is where we wait for input and call the proper function based on it.
    while True:
        print("Available commands: highscore - surrender - exit")
        print("Available helps: prime - even/odd - divisible\n")
        userInput = (input("\nEnter a your guess: ")).lower()
        os.system('clear')

        if userInput.isalpha():

            if (userInput == 'prime'):
                checkPrime(randomNumber)
                numTries += 1

            elif (userInput == "even" or userInput == "odd"):
                checkEven(randomNumber)
                numTries += 1

            elif (userInput == 'divisible'):
                checkDivisible(int(input("Enter the divider: ")), randomNumber)
                numTries += 1

            elif (userInput == "surrender"):
                surrender(randomNumber, numTries)
                randomNumber = restart_game(diff_dictionary[difficulty])

            elif (userInput == "highscore"):
                showHighscore()

            elif (userInput == "exit"):
                print("Goodbye!")
                quit()

            else:
                print(' ' * 8 + "Enter a number or an available command!\n")
        else:
            try:
                int(userInput)

                if (checkGuess(userInput, numTries, randomNumber) == 1):
                    saveHighscore(highscoreList, userName,
                                  numTries, difficulty)
                    time.sleep(3)
                    randomNumber = restart_game(diff_dictionary[difficulty])

            except ValueError:
                print(' ' * 8 + "Enter a number or an available command!\n")


if __name__ == "__main__":
    main()
