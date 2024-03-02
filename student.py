# 2h:28m
class Student:
    def __init__(self, name, house) -> None:

        if house not in ["Jessore", "Khulna", "Bangladesh"]:
            raise ValueError("Invalid House")

        self.name = name
        self.house = house

    def __str__(self) -> str:
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    # print(f"{student.name} from {student.house}")
    print(student)


if __name__ == "__main__":
    main()
