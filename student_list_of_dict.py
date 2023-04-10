students = [
    {'name': 'ram', 'city': 'mumbai', 'pet': 'cat'},
    {'name': 'shyam', 'city': 'Bangalore', 'pet': 'Dog'},
]

for student in students:
    print(student, student['name'], student['city'], student['pet'], sep=', ')