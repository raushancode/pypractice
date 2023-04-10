import sys
import csv
def main():
    output = []
    if len(sys.argv) == 3 and sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        try:
            with open(sys.argv[1], "r") as file:
                lines = csv.DictReader(file)
                for row in lines:
                    split_name = row["name"].split(",")
                    # print(split_name)
                    output.append({"first": split_name[1].lstrip(), "last": split_name[0], "house": row["house"]})

        except FileNotFoundError:
            sys.exit("File does not exist")
        with open(sys.argv[2], "w") as newfile:
            writer = csv.DictWriter(newfile, fieldnames=["first", "last", "house"])
            writer.writerow({"first": "first", "last": "last", "house": "house"})
            for row in output:
                writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    elif not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()