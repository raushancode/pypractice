# checking for even or odd
def main():
    x = int(input("what is the value : "))
    if parity(x):
        print("even")
    else:
        print("odd")

def parity(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()