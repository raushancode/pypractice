def main():

    str = input("camelCase:").strip()
    snake_case(str)

def snake_case(string):
    print("snake_case: ", end="")

    for c in string:
        if c.isupper() == True:
            print("_", end="")# end used to avoid new line
        print(c.lower(), end="")
    print()

main()

