#this is a guess the number game

import random

print('Hello What is your name????')
name = input()


print('Well. ' + name + ', I am thinking of a number between 1 & 20')
secretNum = random.randint(1,20)

for guessesTook in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNum:
        print('Your guess is too low.')
    elif guess > secretNum:
        print('Your guess is too high.')
    else:
        break #Guess is correct!!!

if guess == secretNum:
    print('Great ' + name + '!! you guessed my number in '+ str(guessedTook) + ' guesses!')
else:
    print('Nope . My number is:' + str(secretNum))
    


    
    
