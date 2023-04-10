name = input("what is ur name: ")
file = open("example2.csv", "a")
file.write(name)
file.close()