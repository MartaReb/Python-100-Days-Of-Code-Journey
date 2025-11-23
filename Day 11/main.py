import random
import os
import time
from art import logo

def draw_card():
    card = random.choice(cards)
    return card

def add_card_to_list(list_name):
    card = draw_card()
    list_name.append(card)

def calculate_score(list_cards):
    if 11 in list_cards and sum(list_cards) > 21:
        list_cards.remove(11)
        list_cards.append(1)
    return sum(list_cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 21:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 21:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(logo)
    for i in range(2):
        add_card_to_list(user_cards)
        add_card_to_list(comp_cards)

    user_score = calculate_score(user_cards)
    comp_score = calculate_score(comp_cards)

    while True:
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}")

        answer = input("Type 'y' to get another card, type 'n' to pass: ")
        if answer == 'y':
            add_card_to_list(user_cards)
            add_card_to_list(comp_cards)
            user_score = calculate_score(user_cards)
            comp_score = calculate_score(comp_cards)
        elif answer == 'n':
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print(f"Computer's final hand: {comp_cards},final score: {comp_score}")
            print()
            print(compare(user_score, comp_score))
            time.sleep(5)
            os.system("cls")
            exit()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
comp_cards = []

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system("cls")
    play_game()