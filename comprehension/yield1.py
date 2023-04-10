def main():
    n = int(input("what is n: "))
    for s in sheep(n+1):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * i

if __name__ == "__main__":
    main()