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
