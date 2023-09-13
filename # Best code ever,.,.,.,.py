# Best code ever,.,.,.,.:!!!
# import some shit
import os
import random
import time

randomNumber = random.randint(1,10)

print('Funny game!')
time.sleep (1)

guess = int(input('Try to guess a number between 1 and 10.'))

if randomNumber == guess:
    os.system('cls')
    print('GG! You got it right.')
else:
    os.system('cls')
    print('Grr. Wrong.')