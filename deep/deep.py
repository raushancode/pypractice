

from cs50 import get_string


s = get_string("what is the answer to the Great Question of Life, the Universe and Everything?").strip().upper()
if s == '42' or s == 'FORTY TWO' or s == 'FORTY-TWO':
        print("Yes")
else:
        print("No")
