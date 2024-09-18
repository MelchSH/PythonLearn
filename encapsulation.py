class Person:
    def __init__(self,name,age) -> None:
        self.__name = name
        self.__age = age

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self,value) -> None:
        self.__name = value

    @staticmethod
    def mymethod() -> None:
        print("Hello world")

Person.mymethod()
p1 = Person("Mash","21")
print(p1.Name)
p1.mymethod()