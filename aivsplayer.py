import random
import os
import time


def main():
    os.system('clear')
    print('Think of a number between 0-100.')
    print("Available command:")
    print("h if your number is higher, l if your number lower, y if the computer guess was right")
    numList = [x for x in range(101)]
    min_i = 0
    max_i = 100
    number_of_tips = 0

    while True:
        try:
            guess = random.randint(min_i, max_i)
            number_of_tips += 1

            if (min_i == guess and max_i == guess):
                print('Your number was: ', guess)
                break

            usrInput = input("Is it {}?".format(guess)).lower

            if usrInput == 'y':  # up-down arrow
                print('Your number was: ', guess)
                break

            elif usrInput == 'l':  # left arrow
                max_i = guess - 1

            elif usrInput == 'h':  # right arrow
                min_i = guess + 1
            else:
                print("Use l (lower) and h (higher) or y (Yes) keys.")
        except ValueError:
            print("Heeeey, don't cheat!")
            print("I don't play with cheaters")
            time.sleep(2)
            break

    print("I found your number in " + str(number_of_tips) + " guesses")
    time.sleep(5)
    print("Return to base game...")
    time.sleep(2)
    os.system('python3 guessthenumber.py')

if __name__ == "__main__":
    main()
