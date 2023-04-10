grocery = {}
while True:
    try:

        item = input().upper()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1


    except EOFError:
        sorteddict = sorted(grocery)
        for key in sorteddict:
            print (grocery[key], key)
        break
    # press cntrl+d