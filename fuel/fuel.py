ywhile True:
    fraction = input("Fraction: ")
    try:
        num, den = fraction.split("/")
        x = int(num)
        y = int(den)
        f = x/y
        if f <= 1:
            break
    except (ZeroDivisionError, ValueError):
        pass

p = round(f*100)
if p <= 1:
    print("E")
elif p >= 99:
    print("F")
else:
    print(f"{p}")