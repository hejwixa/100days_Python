def highest_bid():
    highest_bid = 0
    winner = ""
    for bidden in biders:
        bid_amount = biders[bidden]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidden
    print(f"The winner is {winner} with a bid of ${highest_bid}")

biders = {}
running_program = True
while running_program:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    biders[name] = bid
    should_run = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if should_run == "no":
        running_program = False
        highest_bid()
    elif should_run == "yes":
        print("\n" * 40)
