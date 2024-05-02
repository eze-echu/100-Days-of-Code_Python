
import re
from art import logo
import os


def clear():(
    os.system('cls' if os.name == 'nt' else 'clear'))


# This was the function given in the class
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder, bid_amount in bidding_record:
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


if __name__ == "__main__":
    print(logo)
    print("Welcome to the silent auction system")
    pending_players = True
    bids = dict()
    while pending_players:
        player_name = input("What is your name? \n")
        bid = input("What is your bid? \n")
        bids[player_name] = bid
        next = input("is there another bidder left? \n")
        if re.match(r'[no|false]', next, re.IGNORECASE):
            pending_players = False
        elif re.match(r'[yes|true]', next, re.IGNORECASE):
            clear()
    sorted_bids = sorted(bids.items(), key=lambda x: x[1], reverse=True)
    clear()
    print(f"The winner is {sorted_bids[0][0]} with a bid of ${sorted_bids[0][1]}")
