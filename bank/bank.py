from cs50 import get_string
def main():

    s = get_string("Greeting: ").strip().upper()

    if len(s) < 5:
        if s[0] == 'H':
            twenty_dollar()
            exit()
        else:
            hundred_dollar()

    elif len(s) >= 5:

        if s[0] == 'H' and s[1] == 'E' and s[2] == 'L' and s[3] == 'L' and s[4] == 'O':
            zero_dollar()
        elif s[0] == 'H':
            twenty_dollar()
        else:
            hundred_dollar()

def twenty_dollar():
        print("$20")

def hundred_dollar():
        print("$100")

def zero_dollar():
        print("$0")

main()