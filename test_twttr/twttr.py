def main():

    str = input("input:").strip()
    new_str = shorten(str)
    print (new_str)

def shorten(word):

    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    for c in word:
        if c not in vowel:
            result = result + c
    return result

if __name__ == "__main__":
    main()