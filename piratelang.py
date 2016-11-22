"""consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

to_pirate = str(input("Skriv din mening som ska översättas här: "))
output = ""
for char in to_pirate:
    if char in consonants:
        output += char + "o" + char
    else:
        output += char


f = open('pirate.txt', 'r+')
f.write(output)

f.close()
"""
import random
import time

def generator():

    attempts = 3
    number = random.choice(['1', '2', '3', '4', '5'])

    print("Following number was generated: \n" + number)

    for attempts in range(attempts):

    if randomnumber in number:
        print("Congratulations! You can now enter the spaceship!")
    else:
        print("Sorry, but your number was not the generated number.")
        time.sleep(1)
        play = input("Try again? (Y/N)")
        if play == "Y":
            generator()
        else:
            print("Guess you will stay here on planet Earth then. And we all know what that means...")
            time.sleep(2)
            print("Game Over.")
            sys.exit()



generator()


"""
for x in generator:
    if generator in number:
        print("Congratulations!")
    else:
        print("Game over.")
"""

