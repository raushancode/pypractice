class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return(f"{self.name} is from {self.house}")

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("missing name")
        self._name = name
    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["gaya", "patna"]:
            raise ValueError("misssing house")
        self._house = house

def main():
    student = get_student()
    print(student)


def get_student():
    name = input("name : ")
    house = input("house : ")
    student = Student(name, house)
    return student
    # or return Student(name, house)

if __name__ == "__main__":
    main()