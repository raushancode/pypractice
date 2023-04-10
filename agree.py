from cs50 import get_string
s = get_string("do u agree : ").upper()
if s in ["Y", "YES"]:
    print("agreed")

else:
    print("not agreed")

