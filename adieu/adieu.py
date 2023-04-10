names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)

    except EOFError:
        # print()
        break

print("Adieu, adieu, to", end=" ")
if len(names) > 1:
    for i in range(len(names)-1):

        print(names[i], end="")
        if i < len(names)-2:
            print(", ", end="")
        else:
            print(" and " + names[i+1])
            # print()
else:
    print(names[0])
# print()
