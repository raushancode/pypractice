import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("too many arguments")

# print("hello my name is", sys.argv[1])

# for arg in sys.argv[1:]:
#     print("my name is", arg)

for arg in sys.argv:
    print("my name is", arg)