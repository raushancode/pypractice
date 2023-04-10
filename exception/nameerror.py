
def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            x = int(input("what is x ? ")) # int is behaving as function, so if string is paseed, it will give a vlaueerror as string cannot be converted to integer, it will give name error unless use else
            return x
        except ValueError: # we can use multiple exception also
            print ("x is not a integer") # try using pass instead of print
            #pass

main()

#try nameerror after removing else