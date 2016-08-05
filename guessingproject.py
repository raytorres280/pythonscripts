import random
import time
import py2exe


#entire script loop

while 1==1: 
    greeting = print("lets play a game....")
    time.sleep(3)
    print("you have to guess a number between 1 and 100")
    time.sleep(3)
    print("but you only have 10 guesses you do so...")
    time.sleep(3)
    print("make them count")



    mysterynumber = random.randint(1,100)

    guessnumber = 0

    def computing():
        print("calculating...")
        time.sleep(3)

    def linespace():
        print(" ")

    #game loop

    while guessnumber < 10:
        guessnumber = guessnumber + 1
        guess = int(input("What's your guess?"))
        computing()
        if guess == mysterynumber:
            print("congrats! you won")
            break
        elif guess != mysterynumber:
            print("that is incorrect")
            time.sleep(1)
            linespace()
            if guess < mysterynumber and guessnumber != 10:
                  print("guess higher dude")
            elif guess > mysterynumber and guessnumber != 10:
                  print("guess lower dude")
        if guessnumber < 10:
            time.sleep(1)
            linespace()
            print("you have made {} guess(es)".format(guessnumber))
        else:
            print("YOUR GUESSES ARE UP!! GAME OVER!")
            continue
        #guessnumber = guessnumber + 1 <<<<WHY DOESNT IT WORK HERE???

    terminate = input("to close the game type 'DONE', to restart type 'RESTART'")
    if terminate == 'DONE':
            break
    
    elif terminate == 'RESTART':
            continue
        



