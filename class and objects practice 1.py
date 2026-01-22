class student:
    def __init__(self):
        self.name="abrakadabra"
        self.regno="1256"
    def display(self):
        print("Name: ",self.name)
        print("Register Number: ",self.regno)

class otherdetails:
    def __init__(self):
        self.add=""
        self.ph=""
    def display(self):
        print("Address: ",self.add)
        print("Phone Number: ",self.ph)

ajay=otherdetails()
sanjay=student()

ajay.name="Ajay Raghavendar"
ajay.regno="cf 1555"
ajay.add="1, anna st, chennai 78."
ajay.ph="9025880617"

sanjay.name="Jagadeesh"
sanjay.regno="cf 1358"

ajay.display()
print()
sanjay.display()
print()
#---------------------------------------------------------------------
class fruit:
    def __init__(self,col):  #using parameter as "col"
        self.colour=col

apple=fruit("Red")
print(apple.colour)
print()


#------------------------------------------------------------
class teacher:
    def __init__(self,name,regn):
        self.details=(name,regn)
        
t1=teacher("sarala","cf1358")
t2=teacher("Anitha","cf1236")
print(t1.details)
print(t2.details)
#---------------------------------------------------------------------
class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        self.c=self.num1+self.num2
        print("Additon is ",self.c)
    def sub(self):
        self.c=self.num1-self.num2
        print("Substituion is ",self.c)
    def div(self):
        self.c=self.num1/self.num2
        print("Division is: ",self.c)
    def mul(self):
        self.c=self.num1*self.num2
        print("Multiplication of number is: ",self.c)
num=calculator(int(input("No1:")),int(input("No2:")))
choice=input("add, mul, div, sub: ")
if (choice=="add"):
    num.add()
elif(choice=="mul"):
    num.mul()
elif(choice=="div"):

    num.div()
elif(choice=="sub"):
    num.sub()
else:
    print("ERROR 404")






















        







        
        
