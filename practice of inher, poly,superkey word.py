#1. create a base called sgape with a method area() that return 0.
#crea a derived class called rectangle that inherites from shape and overrides the area()
#method to calcuaate and return  the area of a rectangle
class shape():
    def area(self):
        return 0

class rectangle(shape):
    def area(self,l=1,b=1):
        print("Area of retangle is ",l*b)

s1=shape()
print(s1.area())
r1=rectangle()
r1.area(5,5)
print()

#2. createe a base cls called perso with a conswtructor that takes a name
#as a parameter. create a derived cls called student that inherits from
#person and has a constructor that takes a parameter called graduate.
#write a method in student to display the name and graduate of the student
#Use superdeyword to achieve this.
class person():
    def __init__(self,name):
        self.name=name

class student(person):
    def __init__(self,name,graduate):
        super().__init__(name)          #calling parent class construtor
        self.graduate=graduate

    def display(self):
        print("Name: ",self.name)
        print("UG: ",self.graduate)
        

vishal=student("Vishaal","BCA")
vishal.display()
print()

#3. Create a base cals acalled vehicle with a method start() that prints"vehiclses tarted".
#create a derived cls called car that inherits fdrom vehicle and overrides that start() method to print("Car started")
class vehicle():
    def start(self):
        print("Vehicle started")

class car(vehicle):
    def start(self):
        print("Car started")

tata=car()
tata.start()
print()  

#4. Create a base cls employee with properties name and salary. create a derived cls called
#manager that inherites from employee and adds a property department. write a method in manager
#to display the name, salary, and department of the manager.
class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department

    def display(self):
        print(self.name,self.salary,self.department)

suresh=Manager("Sureshgovind","40000","QC")
suresh.display()






















