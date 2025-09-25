#Lab 1
#Group # 1
#Authors: Shriyash
#       : Luke
#Date: 09/23/25
import random


# Guessing Game : Program generates a number b/w [1,100] that the user tries to guess, Each user has 5 tries to get it right.
# Author : Shriyash
count = 5
def guess_game():
    global count
    count = 5
    random_num =  random.randint(1, 100)
    one_try_guess(random_num)


def one_try_guess(random_num):
    user_guess = take_guess()
    check_guess(random_num, user_guess)



def decrease_count():
    global count
    count -=1

def take_guess():
     user_guess = int(input("Guess a number between 1 and 500: "))
     return user_guess

def check_guess(random_num, user_guess, ):

    if user_guess == random_num:
        print( "You won!!")
    elif user_guess > random_num:
        print("Too high!!")
        if count != 0:
            print("Guess Again " + str(count) + " tries left")
            decrease_count()
            one_try_guess(random_num)

    else:
         print("Too low!!")
         if count != 0:
             print("Guess Again " + str(count) + " tries left")
             decrease_count()
             one_try_guess(random_num)

guess_game()