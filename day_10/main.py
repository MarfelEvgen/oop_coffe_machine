from replit import clear
import random
from game_data import data
from art import *

def random_choice():
    return random.choice(data)

def seleb_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f'{name}, a {description}, from {country}'

def win_seleb(a, b):
    if a > b:
        return a
    else:
        return b

def double_check(a, b):
    if a == b:
        b = random_choice()
    return b

def game_name():
    game_continue = True
    score = 0

    while game_continue:
        seleb_a = random_choice()
        seleb_b = random_choice()

        double_check(seleb_a, seleb_b)

        follower_a = seleb_a['follower_count']
        follower_b = seleb_b['follower_count']
        guess = win_seleb(follower_a, follower_b)

        print(f"Compare A: {seleb_data(seleb_a)}.")
        print(vs)
        print(f"Compare A: {seleb_data(seleb_b)}.")
        answer = input("'Who has more followers? Type 'a' or 'b':\n")
        if answer == 'a':
            answer = follower_a
        else:
            answer = follower_b

        if answer == guess:
            score += 1
            print(f'Wery good.\nCurrent score: {score}')
            clear()

        else:
            print(f"Sorry, that's wrong.\nFinal score: {score}")
            game_continue = False

print(logo)
game_name()




