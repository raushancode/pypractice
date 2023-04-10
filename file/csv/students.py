students = []
with open("students.csv") as file:
    for line in file:
        name1, city1, type1 = line.strip().split(",")
        # student = {}
        # student["name"] = name1
        # student["city"] = city1
        # student["type"] = type1
        # or we can use
        student = {"name": name1, "city": city1, "type": type1}
        students.append(student)

print(students)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['city']} and city type is {student['type']}")

    # alternate method to sort
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['city']} and city type is {student['type']}")