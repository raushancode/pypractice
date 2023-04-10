
def parity(n):
    return n % 2 == 0



x = int(input("what is the value : "))
if parity(x):
    print("even")
else:
    print("odd")

