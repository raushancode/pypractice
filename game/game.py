import random
def main():
    l = level()
    g = guess()

    rr = random.randint(1,100)

    if g < rr:
        print("Too small!")
    elif g > rr:
        print("Too large!")
    else:
        print("Just right!")
    




def level():

    while True:

        try:
            n = int(input("Level: "))
            if n < 1:
                continue
        except :
            continue
        return n
def guess():

    while True:
        try:
            g = int(input("Guess: "))
            if g < 1:
                continue
        except:
            continue
        return g

main()

