def showHighscore():

    cache = list()
    my_file = (open("highscore.txt", mode='r'))
    for line in my_file:
        cache.append(line.strip())
    my_file.close()

    print("Highscores:")
    print('Name'.rjust(16) + ' ' * 3 + 'Score')
    print('-' * 25)
    for i in range(0, len(cache)):

        print((cache[i].split(sep=": "))[0].rjust(16), end='')
        print((cache[i].split(sep=": "))[1].rjust(6))
    print('-' * 25)


def saveHighscore(highscoreList, name, score, dif):

    my_file = (open("highscore.txt", mode='r'))

    for line in my_file:
        highscoreList.append(line.strip().split(': '))
    my_file.close()

    highscoreList.append([name + dif, str(score)])
    highscoreList.sort(key=lambda x: int(x[1]))

    my_file = (open("highscore.txt", mode='w'))
    for j in range(0, int(len(highscoreList))):
        my_file.write(": ".join(highscoreList[j]) + "\n")
    my_file.close()

showHighscore()
