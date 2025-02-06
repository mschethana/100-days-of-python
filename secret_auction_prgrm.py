next='yes'
bidders={}
print("Welcome to the secret auction program")

while next=='yes':
    name=input("\n What is your name?: ")
    bid=int(input("\nWhat is your bid?: "))
    bidders[name]=bid
    next=input("Are there any other bidders? Type 'yes' or 'no' ")
    print("\n"*100)

highest_bid=0
highest_bidder=''

for name in bidders:
    if bidders[name]>highest_bid:
        highest_bid=bidders[name]
        highest_bidder=name
print(f"The winner is {highest_bidder} with a bid of {highest_bid}") 
    


