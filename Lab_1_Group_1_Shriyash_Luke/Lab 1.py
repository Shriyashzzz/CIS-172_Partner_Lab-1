# Lab 1
# Group # 1
# Authors: Shriyash
#       : Luke
# Date: 09/23/25
import random
from warnings import catch_warnings

# Guessing Game
# Description: Program generates a number b/w [1,100] that the user tries to guess, Each user has 5 tries to get it right.
# Author : Shriyash
count = 5


def guess_game():
    global count
    count = 5
    random_num = random.randint(1, 100)
    one_try_guess(random_num)


def one_try_guess(random_num):
    user_guess = take_guess()
    check_guess(random_num, user_guess)


def decrease_count():
    global count
    count -= 1


def take_guess():
    user_guess = int(input("Guess a number between 1 and 500: "))
    return user_guess


def check_guess(random_num, user_guess, ):
    if user_guess == random_num:
        print("You won!!")
        ask_if_play_again(2)
    elif user_guess > random_num:
        print("Too high!!")
        if count != 0:
            print("Guess Again " + str(count) + " tries left")
            decrease_count()
            one_try_guess(random_num)
        else:
            print("You ran out of tries, the number was: : " + str(random_num))
            ask_if_play_again(0)


    else:
        print("Too low!!")
        if count != 0:
            print("Guess Again " + str(count) + " tries left")
            decrease_count()
            one_try_guess(random_num)
        else:
            print("You ran out of tries, the number was: " + str(random_num))
            ask_if_play_again(0)

def ask_if_play_again(game_num):
    user_choice = str(input("Do you want to play again? (y/n): "))
    if user_choice.lower() == "y":
        if game_num == 0:
            guess_game()
        elif game_num ==1:
            rock_paper_scissors()
        elif game_num == 2:
            main_menu()
    else:
        return


# Rock Paper Scissors
# Author: Luke
# Description : User gets to choose rocl/paper/scissor and plays against the computer's choice.
def rock_paper_scissors_win_conditions(winner, loser):
    if winner == 1 and loser == 3:  
        return True
    elif winner == 2 and loser == 1:
        return True
    elif winner == 3 and loser == 2:
        return True
    else:
        return False


def rock_paper_scissors():
    choice = ''
    bot = random.randint(1, 3)
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

    while choice not in [1, 2, 3]:
        choice = int(input('Enter your choice: 1. Rock, 2. Paper, 3. Scissors: '))
        if choice not in [1, 2, 3]:
            print('Please input 1, 2, or 3.')
        else:
            print(f"You chose: {choices[choice]}")
            print(f"Computer chose: {choices[bot]}")

            if choice == bot:
                print('It is a tie!')
                ask_if_play_again(1)
            elif rock_paper_scissors_win_conditions(choice, bot):
                print('You win!')
                ask_if_play_again(2)
            else:
                print('You lose!')
                ask_if_play_again(1)


# Main Menu
#Description: an starting point for the game, where a user can choose b/w either of the games
# noinspection PyUnboundLocalVariable
def main_menu():
    print("Welcome Player, what would you like to play?")
    print("1. Rock Paper Scissors")
    print("2. Guess Game")
    try:
        user_choice = int(input("Enter your choice(1 or 2): "))
    except ValueError:
        print("Please input a number (1 for rock paper scissors, 2 for guess game).")
        main_menu()
    if user_choice ==1:
        rock_paper_scissors()
    elif user_choice == 2:
        guess_game()

if __name__ == '__main__':
    main_menu()