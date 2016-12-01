groceries = ["banana", "orange","apple"]
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}


prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
#1st

##def compute_bill(x):    
##    total=0
##    total += prices[x]
##    return(total)
##print(compute_bill("banana"))

#2 Edited

def compute_bill(x):
    total = 0
    if stock[x]>0:
        total += prices[x]
        stock[x] = stock[x]-1
    else:
        print("Out of stock")
    return(total)
buy = input("Do you want some fruits? (Y/N)")
bill = 0
while buy.lower() == "y":
    fruit = input("Which fruit do you want to buy? ")
    money = compute_bill(fruit)
    bill +=money
    print("Your bill is: ",bill)
    print(fruit,"in stock: ",stock[fruit])
    buy = input("Do you want some fruits? (Y/N)")
