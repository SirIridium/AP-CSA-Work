import random
import time
#a funchtion that I know tells to wait x seconds
def holdup(timetowait):
    time.sleep(timetowait)
    return
favoriteNumber=42
favoriteColor='blue'
#prints the bots favorite number (pseudo random) 
print("Press control+C to end the loop")

holdup(1.5)
name = input("What is your name?")
holdup(1)
print("Hello " + name + "!")

holdup(1)
print("")
holdup(.75)
print("My name is Luke Bushell, and This is my AP CSA project!")
holdup(.5)
print("")
holdup(1.5)
print("I'll tell you about a few things, Sea Base, Summer Camp, or, Working Staff, Favorite Number, Favorite Color")
holdup(1)
print("")
holdup(1)


def WhatKnow():
    
    while True:
        print("I had a very eventful summer, what would you like to know about first? Please use numbers to indicate which, 1 being Sea Base and so on to 5. ")
        holdup(.5)
        print("")
        holdup(.75)
        firstPrompt = input("Enter what you want to know about here: ")
        holdup(1)
        if(int(firstPrompt)==1):
            print("")
            holdup(.5)
            print("I went to a summer camp called sea base where you go on boats and explore the ocean, sadly my vacation was cut short by a concussion")
            holdup(1)
            print("")
            holdup(1)

        elif(int(firstPrompt)==2):
            print("")
            holdup(.5)
            print("I went to a summer camp, a week long camp, and they liked me a lot, so I was invited back as a staff, see 3")
            holdup(1)
            print("")
            holdup(1)

        elif(int(firstPrompt)==3):
            print("")
            holdup(.5)
            print("I was invited back as a staff member in training for another 3 weeks to this summer camp, and I was happy to be back, however around week 2, I got the conucussion and that wasn't super fun, the program for training staff is super fun though.")
            holdup(1)
            print("")
            holdup(1)

        elif(int(firstPrompt)==4):
            print("")
            holdup(.5)
            print("You have to guess my favorite number. It is related to a book written by Douglas Adams.")
            holdup(.5)
            print("")
            while True:
                holdup(.5)
                numGuess = input("Try a guess here: ")
                if (int(numGuess)==favoriteNumber):
                    holdup(1)
                    print("Hey, you got it! The answer to life the universe and everything!")
                    break
                elif(int(numGuess)>=favoriteNumber):
                    holdup(1)
                    print("Don't get too ambitious, try a little lower.")
                elif(int(numGuess)<=favoriteNumber):
                    holdup(1)
                    print("Thats not qite it, try a little higher.")

            print("")
            holdup(1)
        elif(int(firstPrompt)==5):
            print("")
            holdup(.5)

            print("You have to guess my favorite color now! No hints this time!")
            holdup(.5)
            print("")
            while True:
                holdup(.5)
                colGuess = input("Try a guess here: ")
                holdup(.5)
                print("")
                if (colGuess == "blue"):
                    holdup(.5)
                    print("Thats my favorite color! It was kind of assigned to me as a baby when my mother always made me wear blue, because I am a twin.")
                    break
                elif(colGuess != "blue"):
                    holdup(.5)
                    print("Thats not quite it, keep going!")
            holdup(1)
            print("")
            holdup(1)
WhatKnow()

#test
