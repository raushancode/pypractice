def main():
    n = int(input("what is n: "))
    for s in sheep(n+1):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
        # print (flock)
    return flock

if __name__ == "__main__":
    main()