price = []
with open("regular.csv", "r") as file:
    # lines = file.readlines()
    # print(lines)
    for line in file:
        # print(line, end="")
        price.append(line)
print(price)
print(sorted(price))
for rate in sorted(price):
    print(rate)