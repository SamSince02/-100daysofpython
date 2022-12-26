from replit import clear

from art import logo
print(logo)

bids = {}
condition = False

def find_highest_bidder(bids):
  highest_bidder = 0
  winner= ""
  for bidder in bids:
    bidding_amount = bids[name]
    if bidding_amount> highest_bidder:
      highest_bidder = bidding_amount
      winner = name
  print(f"The highest bidder is {winner} with the bid of {highest_bidder} ")

while not condition:
  name = input("What is your name? \n")
  bid = int(input("What is your bid? \n"))
  
  bids[name] = bid
  inputs = input("Type yes if anyone is present or type no ")
  if inputs == "no":
    condition= True
    find_highest_bidder(bids)
  elif inputs == "Yes":
    clear()
  else:
    print("Invalid inputs")
    condition=True
    
