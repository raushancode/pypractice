import random
def main():
    level = get_level()
    i = 0
    while i < 5:

            x = get_integer(level)
            y = get_integer(level)
            get_output(x,y)
            i += 1
            continue




def get_output(x,y):
    error = 0
    # score = 0
    while error < 3:
        try:
            ans = int(input(f"{x} + {y}: "))
            if ans >= 0 and ans == x + y:
                break
                # return score
            else:
                print("EEE")
                error += 1
                continue

        except:
            print("EEE")
            error += 1
            continue
    print((f"{x} + {y}:"),x + y)



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level <4:
                return level
        except:
            continue

def get_integer(level):
    if level == 1:
        a = random.randint(0,9)

    elif level == 2:
        a = random.randint(10,99)

    elif level == 3:
        a = random.randint(100,999)

    return a

def get_integer(level):
    if level == 1:
        b = random.randint(1,9)

    elif level == 2:
        b = random.randint(10,99)

    elif level == 3:
        b = random.randint(100,999)

    return b



main()

