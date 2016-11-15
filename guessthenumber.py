import os
import random
import sys


def checkGuess(userInput, name, score):
    if (int(userInput) == randomNumber):
        print("Your guess was right!")
        saveHighscore(highscoreList, name, score)
        numTries += 1

    elif (int(userInput) > randomNumber):
        print("The number is smaller!")
        numTries += 1

    elif (int(userInput) < randomNumber):
        print("The number is bigger!")
        numTries += 1


def showHighscore():
    cache = list()
    my_file = (open("highscore.txt", mode='r'))
    for line in my_file:
        cache.append(line.strip())
    my_file.close()

    print("Highscores: ")
    for i in range(0, len(cache)):
        print(cache[i])


def saveHighscore(highscoreList, name, score):
    my_file = (open("highscore.txt", mode='r'))

    for line in my_file:
        highscoreList.append(line.strip().split(': '))
    my_file.close()

    highscoreList.append([name, str(score)])
    highscoreList.sort(key=lambda x: int(x[1]))

    my_file = (open("highscore.txt", mode='w'))
    for j in range(0, int(len(highscoreList))):
        my_file.write(": ".join(highscoreList[j]) + "\n")
    my_file.close()


def generateNewNumber():
    randnumber = random.randint(0, 100)
    return randnumber


def surrender(random_num, numTries):
    print("The number was: " + str(random_num))
    print("The number of your tries: " + str(numTries))
    print('\nGenerating new number')
    os.system("eject cdrom")  # easteregg


def checkEven(randomNumber):
    if((randomNumber % 2) == 0):
        print("It is even!")  # its even
    else:
        print("It is odd!")  # its odd


def checkDivisible(input, randomNumber):
    if((randomNumber) % input == 0):
        return True
    else:
        return False


def checkPrime(randomNumber):
    primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    if randomNumber in primeList:
        return True
    else:
        return False


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
                userQuestion = input("\nAvailable helps: ").lower()

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
