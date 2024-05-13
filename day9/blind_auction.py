from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bids = {}
bidding_finished = False


def add_bid(name, bid):
    bids[name] = bid
    return bids

while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    add_bid(name, bid)
    question = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if question == "no":
        bidding_finished = True
        clear()
    elif question == "yes":
        clear()

highest_bid = 0
winner = ""
for bid in bids:
    if bids[bid] > highest_bid:
        highest_bid = bids[bid]
        winner = bid
print(f"The winner is {winner} with a bid of ${highest_bid}.")
