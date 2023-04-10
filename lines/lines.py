import sys

def main():
    if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):

        try:
            with open(sys.argv[1], "r") as file:
                lines = file.readlines()
                count = read_lines(lines)
                print(count)

        except FileNotFoundError :
            sys.exit("File does not exist")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Not a Python file")

def read_lines(lines):
    count = 0
    for line in lines:
        if line.startswith("#") or line.isspace() or line.startswith('"""') or line.startswith("'''"):
            # print("true")
            continue
        else:
            count += 1
    return count
if __name__ == "__main__":
    main()
