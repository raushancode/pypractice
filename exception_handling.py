def main():
    x = get_int('what is x? ')
    print(f"x is {x}")

def get_int(prompt):

    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print('x is not an integer') # we can use pass also, it won't show msg
        else:
            return x #it will return and break out of loop
main()
