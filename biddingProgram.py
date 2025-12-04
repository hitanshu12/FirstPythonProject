



def find_highest_bidder(bidder_details):
    winner = ""
    highest_bid = 0
    for bid in bidder_details:
        bid_amount = bidder_details[bid]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bid

    print(f"The winner is {winner} with a bid of ${highest_bid}")

bidder_details ={}
continue_bidding = True

while continue_bidding:
    key = input("What is your name? \n").lower()
    value = int(input("Whis is your bid: $"))
    bidder_details[key] = value
    bidders = input("Are there any other bidders? Type 'Yes' or 'No' \n").lower()

    if bidders == "no":
        continue_bidding = False
        find_highest_bidder(bidder_details)
    elif bidders == "yes":
        print("\n " * 100)

