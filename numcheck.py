import math


def checkEven(randomNumber):
    if((randomNumber % 2) == 0):
        print("It is even!")  # its even
    else:
        print("It is odd!")  # its odd


def checkDivisible(input, randomNumber):
    if((randomNumber) % input == 0):
        print("It is divisible by {}.\n" .format(input))
    else:
        print("It is not divisible by {}.\n" .format(input))


def checkPrime(randomNumber):
    for i in range(2, int(math.sqrt(randomNumber))):
        if randomNumber % i == 0:
            print('Not a prime number.')
            break
    else:
        print('Yes, it is a prime number.')

checkPrime(22)
