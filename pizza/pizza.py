from tabulate import tabulate
import sys
import csv
def main():
    if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
        try:
            with open(sys.argv[1], "r") as file:
                # lines = file.readlines()
                lines = csv.reader(file)
                for row in lines:
                    print(tabulate(lines, headers="firstrow", tablefmt="grid"))
        except:
            sys.exit("File does not exist")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
