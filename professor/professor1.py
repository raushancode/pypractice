import random
def main():
    get_output()
    # print("score:", score)


def get_output():
    score = 0
    i = 0
    level = get_level()
    while i < 5:
        error = 0
        x = get_integer(level)
        y = get_integer(level)
        while error < 3:
                try:
                    ans = int(input(f"{x} + {y}: "))
                    if ans >= 0 and ans == x + y:
                        score += 1
                        break
                    else:
                        print("EEE")
                        error += 1
                        if error == 3:
                            print(f"{x} + {y}:", x + y)
                            continue
                except:
                    print("EEE")
                    error += 1
                    if error == 3:
                        print(f"{x} + {y}:", x + y)
                        continue
        # print(f"{x} + {y}:", x + y)
        i += 1
    print("score", score)






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


if __name__ == "__main__":
    main()

