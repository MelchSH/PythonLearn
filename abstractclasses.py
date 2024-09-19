from abc import ABC,abstractmethod

class IPerson(ABC):
    @abstractmethod
    def person_method():
        pass

class Student():
    def __init__(self) -> None:
        pass
    def person_method(self):
        print("Im a student")

class Teacher():
    def __init__(self) -> None:
        pass
    def person_method(self):
        print("Im a teacher")

class Person_builder:
    @staticmethod
    def get_person(person_type:str):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        return -1


if __name__ == "__main__":
    choice = input("Teacher or student?\n")
    person = Person_builder.get_person(choice)
    person.person_method()