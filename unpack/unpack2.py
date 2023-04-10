def main():
    yell("i", "am", "rau")

def yell(*words):
    print(*words)
    print(words)
    # uppercased = map(str.upper, words)
    uppercased = [word.upper() for word in words]
    '''
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    '''
    print(uppercased)
    print(*uppercased)
if __name__ == "__main__":
    main()