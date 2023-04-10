class Student:
    ...

def main():

    student = get_student()
    print(f"{student.name} is from {student.city}")



def get_student():
    student = Student()
    student.name = input("name")
    student.city = input("city")
    return student



if __name__ == "__main__":
    main()