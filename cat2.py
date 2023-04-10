while True:
    n = int(input("enter the value of n ? "))
    if n > 0:
        break

for _ in range(n):
    print('meaw')

# using function

print('using function')

def main():
    meaw(n)

def meaw(n):
    for _ in range(n):
        print('meaw')
main()