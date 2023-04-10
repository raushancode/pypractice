import sys

if len(sys.argv) < 2:
    print("few more arguments")
elif len(sys.argv) > 2:
    print("few less arguments")
else:
    print("my name is", sys.argv[1]) # use "" for more argument