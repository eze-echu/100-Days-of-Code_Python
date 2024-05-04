import random
from art import logo
import re
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def game_over() -> bool:
    retry = input("Game Over\n Retry? (y/n)")
    if retry == "y":
        return True
    else:
        return False


def check_result(hand1: list, hand2: list):
    if sum(hand1) > 21 or sum(hand2) > sum(hand1):
        return False
    elif sum(hand2) > 21 or sum(hand1) > sum(hand2):
        return True


def check_blackjack(hand: list):
    if sum(hand) == 21:
        return True
    else:
        return False


def check_over(hand: list):
    if sum(hand) > 21:
        return True
    else:
        return False


def start():
    player_hand = random.choices(cards, k=2)
    computer_hand = random.choices(cards, k=2)
    print(f"Your hand: {player_hand}\nTotal: {sum(player_hand)}")
    print(f"Computer hand: {computer_hand}\nTotal: {sum(computer_hand)}")
    while True:
        if not check_blackjack(player_hand) and not check_blackjack(computer_hand):
            action = input("Hit or Stand?\n")
            if re.match(r"[Hh]it", action, re.IGNORECASE):
                new_card = random.choice(cards)
                player_hand.append(new_card)
                print(f"New card: {new_card}\nYour hand: {player_hand}\nTotal: {sum(player_hand)}")
                if check_over(player_hand):
                    return "Over 21, You Lose!"
                elif check_blackjack(player_hand):
                    return "Blackjack, You Win!"
            if sum(computer_hand) < sum(player_hand):
                new_card = random.choice(cards)
                computer_hand.append(new_card)
                print(f"New card: {new_card}\nComputer hand: {computer_hand}\nTotal: {sum(computer_hand)}")
                if check_over(computer_hand):
                    return "Over 21, You Win!"
                elif check_blackjack(computer_hand):
                    return "Blackjack, You Lose!"
            if sum(computer_hand) == sum(player_hand):
                return "Tie, House Wins!"
        elif check_blackjack(player_hand):
            return f"Blackjack, You Win!"
        else:
            return f"Blackjack, You Lose!"


if __name__ == "__main__":
    play = True
    while play:
        print(start())
        play = game_over()
        clear()



