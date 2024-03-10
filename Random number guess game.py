# Random number guess game
import random

number = random.randint(0,10)
guess =0
  
 

while guess!=number:
    
    guess =int(input("The number"))

    if (guess <number):
       print("Guess higher")
    elif (guess>number):
       print("Guess lower")
    else:
       print("excellent")
       