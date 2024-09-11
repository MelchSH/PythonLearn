class Person:

    amountPeople = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amountPeople += 1 

    def __str__(self):
        return ("Name: {}, Age: {}, Height: {}".format(self.name,self.age,self.height))
    
    def get_older(self, years):
        self.age += years

class Worker(Person):
    def __init__(self, name, age, height, salary):
        super().__init__(name,age,height)
        self.salary = salary
    
    def __str__(self):
        text = super().__str__()
        text += ", Salary: {}".format(self.salary)
        return text

    def calc_yearly_salary(self):
        return self.salary
worker1 = Worker("Melch","21","1.70",10000)

print(worker1.name, worker1.age,worker1.calc_yearly_salary())

print(f"\n",worker1)
