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

# Rock Paper Scissors
# Author: Luke
def rock_paper_scissors_win_conditions(winner,loser):
    if winner==1 and loser==3:
        return(True)
    elif winner>loser:
        return(True)
    else:
        return(False)
        
def rock_paper_scissors():
    choice=''
    bot=random.randint(1,3)
    while choice!=1 and choice!=2 and choice!=3:
        choice=int(input('Enter your choice: 1. rock, 2. paper, 3. scissors '))
        if choice!=1 and choice!=2 and choice!=3:
            print('Please input 1, 2, or 3.')
        else:
            if choice==bot:
                print('It is a tie!')
            elif rock_paper_scissors_win_conditions(choice,bot):
                print('You win!')
            else:
                print('You lose!')
