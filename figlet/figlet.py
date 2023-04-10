import random
import sys
from pyfiglet import Figlet
figlet = Figlet(font=sys.argv[1])
str = input("Input: ")
print(figlet.renderText(str))