def main():

    Plate = input("Plate:").upper()
    if is_valid(Plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    number = [0,1,2,3,4,5,6,7,8,9]
    if 7 > len(s) > 1:
        if s[0] != '0':
            if s[0:1] not in number:
                i = 2
                x = len(s)
                if x > 2:
                    if s[x-1] not in number:
                        
                        return True
    else:
        return False


main()


