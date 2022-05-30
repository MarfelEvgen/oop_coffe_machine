from replit import clear
import random
from game_data import data
from art import *


def win_seleb(a, b):
    if a > b:
        return a
    else:
        return b

def game_name():
    seleb_a = random.choice(data)
    seleb_b = random.choice(data)
    follower_a = seleb_a['follower_count']
    follower_b = seleb_b['follower_count']
    game_continue = True
    p = win_seleb(follower_a, follower_b)
    score = 0

    while game_continue:
        print(f"Compare A: {seleb_a['name']}, a {seleb_a['description']}, from {seleb_a['country']}{follower_a}")
        print(vs)
        print(f'Compare B: {seleb_b["name"]}, a {seleb_b["description"]}, from {seleb_b["country"]}{follower_b}')
        answer = input("'Who has more followers? Type 'a' or 'b':\n")
        if answer == 'a':
            answer = follower_a
        else:
            answer = follower_b

        if answer == p:
            score += 1
            print(f'Wery good.\nCurrent score: {score}')
            clear()

        else:
            print(f"Sorry, that's wrong.\nFinal score: {score}")
            game_continue = False


print(logo)
game_name()





