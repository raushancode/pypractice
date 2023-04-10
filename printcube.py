def main():
    print_cube(3)

def print_cube(size):
    for i in range(size):
        print_row(size)

def print_row(size):
    print("#" * size)

main()