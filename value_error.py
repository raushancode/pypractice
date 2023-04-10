try:
    x = int(input('what is x? '))
    print('x is', x)
    # using formatted string
    print(f'x is {x}')
except ValueError:
    print('x is not an integer')