#random number guess game

import random

print ('What is your name')
name = input()

print ('Hi ' + name +'. Guess a number between 1 and 20')
secretNumber = random.randint(1,20)


for guessesTaken in range (1,7) :
       print ('Take a guess')
       guess = int (input ())

       if guess < secretNumber :
           print (' your guess is low')
       elif guess > secretNumber :
           print ('your guess is to high')
       else:
                break # correct guess

if guess == secretNumber:
    print ('Good Job ' + name +' it took you ' + str(guessesTaken) + ' guesses')
else:
    print ('The right number was ' + str(secretNumber) + ' You failed ')
