students = ["ram", "shyam", "mahesh"]

new_student = {student: "mumbai" for student in students}

new_student1 = [{"name": student, "city": "mumbai"} for student in students]

print(new_student)
print(new_student1)