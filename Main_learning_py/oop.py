class Person:

    amountPeople = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amountPeople += 1 

    def __str__(self):
        return ("Name: {}, Age: {}, Height: {}".format(self.name,self.age,self.height))

    def __del__(self):
        print("Person deleted :C")
        Person.amountPeople -= 1

person1 = Person("Mash","21","1.70")

print(person1.name)
print(person1.age)
print(person1.height)

person1.name = "SuperPro"
print(person1.name)

person2 = Person("Romy","8","0.6")

print(person1)

print(Person.amountPeople)

del person1

print(Person.amountPeople)
