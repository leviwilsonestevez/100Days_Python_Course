from turtle import clear

from art import logo

print(logo)

bids = {}
auction_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner_bidder = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner_bidder = bidder
    print(f"The winner is {winner_bidder} with a bid of ${highest_bid}")


while not auction_finished:
    name = input(f"What is your name ?: \n")
    price = float(input("What is your bid ? $ : \n"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes(y) or 'no(n)'.\n")
    if should_continue == "no" or should_continue == "n":
        auction_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes" or should_continue == "y":
        clear()
