from replit import clear
import art

print(art.logo)
print("Welcome to the secret auction program\n")

bids = {} #create dictionary for name to be key and the bid to be the value 

resultNum = 0
resultName = ""

while True: # always repeat until the user say no more bidders
  
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  otherBidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

  bids[name] = bid
  
  if(otherBidders=='no'):
    break
  
  clear()

for name, bid in bids.items(): # key (key, value) tuples 
  if bid > resultNum: # highest bid
    resultNum = bid
  
  if resultNum == bid: # highest bidder
    resultName = name

print(f"The highest bidder is {resultName} with ${resultNum}!")
