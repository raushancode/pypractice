mrp = 50
print("Amount Due:", mrp)

while True:
    coin = int(input("Insert Coin:"))
    if(coin >= mrp):
        print("change owed:", coin-mrp)
        break
    else:
        mrp = mrp-coin
        print("Amount Due:", mrp)

