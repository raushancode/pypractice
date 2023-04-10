import datetime
import re
import sys
import inflect


def main():
    birth_date = input("Date of Birth: ")
    try:
        (year, month, day) = check_birthday(birth_date)
    except:
        sys.exit("Invalid Date")

    date_of_birth = datetime.date(int(year), int(month), int(day))
    date_of_today = datetime.date.today()
    # print(date_of_birth, date_of_today)
    diff = date_of_today - date_of_birth
    total_minutes = diff.days * 24 * 60
    # print("Total minutes: ", total_minutes)
    p = inflect.engine()
    # capitalize is used for capitalize 1st char
    print(p.number_to_words(total_minutes, andword=0).capitalize() + " minutes")

def check_birthday(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return (year, month, day)

if __name__ == "__main__":
    main()