from game_data import data
import art
import random
import os
import time

def draw_account():
    index_account = random.randint(0, len(data) - 1)
    return index_account

def make_description(account):
    description = f"{data[account]["name"]}, {data[account]["description"]}, from {data[account]["country"]}"
    return description

score = 0
account_B = draw_account()

while True:
    account_A = account_B
    account_B = draw_account()
    if account_A == account_B:
        account_B = draw_account()

    print(art.logo)
    print(f"Compare A: {make_description(account_A)}")
    print(art.vs)
    print(f"Against B: {make_description(account_B)}")

    followers_count_A = data[account_A]["follower_count"]
    followers_count_B = data[account_B]["follower_count"]

    user_guess  = input("Who has more followers? Enter A or B: ").upper()
    if (user_guess == "A" and followers_count_A > followers_count_B) or (user_guess == "B" and followers_count_A < followers_count_B):
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        print(f"Sorry, you are wrong! Final score: {score}")
        break
    time.sleep(4)
    os.system("cls")
    