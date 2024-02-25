# 1h:48m
class Student:
    def __init__(self, name, house) -> None:

        if house not in ["Jessore", "Khulna", "Bangladesh"]:
            raise ValueError("Invalid House")

        self.name = name
        self.house = house

    def __str__(self) -> str:
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Jessore", "Khulna", "Bangladesh"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    # print(f"{student.name} from {student.house}")
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
