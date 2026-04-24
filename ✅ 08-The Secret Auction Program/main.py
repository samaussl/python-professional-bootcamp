from art import logo

print(logo)

def find_highest_bidder(bidding_log):
    highest_bid = 0
    winner = ""

    for bidder in bidding_log:
        bid_amount = int(bidding_log[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f" The winner is {winner} with a bid of ${highest_bid}")


bids = {}
continue_bidding = True

while continue_bidding:
    name = input ("What is your name?\n ")
    price = input ("What is your bid?\n ")

    bids[name] = price

    more_bids = input("Are there any other bidders? Type 'yes or no'.\n")

    if more_bids == "no":
        continue_bidding = False
        find_highest_bidder(bids)
        break
    elif more_bids == "yes":
        print("\n" * 20)

    else:
        print("You entered an invalid option. Please try again.")
        continue
