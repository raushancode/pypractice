menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_value = 0
while True:
    try:
        food = input("item: ").title()
        if food in menu:
            total_value = total_value + menu[food]
            print("Total: $", end=(""))
        print(total_value)
    except EOFError:
        break