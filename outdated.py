list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        mm, dd, yy = date.split("/")
        if ((1 <= int(mm) <= 12) and (1 <= int(dd) <= 31)):
            break

    except:
        try:
            old_mm, old_dd, old_yy = date.split(" ")
            # find month from list
            for i in range(len(list)):
                if old_mm == list[i]:
                    mm = i+1
                    dd = old_dd
                    yy = old_yy
            # remove comma from day
            dd = old_dd.replace(",","")
            if ((1 <= int(mm) <= 12) and (1 <= int(dd) <= 31)):
                break
        except:
            print()
            pass
# int(mm)
# int(dd)
print(f"{yy}-{int(mm):02}-{int(dd):02}")



