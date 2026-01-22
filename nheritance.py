#single inheritance
class dad():
    def phone(self):
        print("Dads phone")

class son(dad):      #Inheriting dad cls into the son clas
    def lap(self):
        print("Son's lap")

ram=son()    #object created for class n
ram.phone()  # bt calling phone function which is in dad's class
print()

#Multilevel inheritance-----------------------------------------
print("Multi:")
class grandpa():
    def ph(self):
        print("Grand's phone")

class dad(grandpa):            #dad class now access grandpa class's fuctions
    def lap(self):
        print("Papa's laptop")

class son(dad):                 #since, dad's class is accessing grandpa's class, so,son class now can access both dad & granpa's class.
    def tab(self):
        print("Son's Tablet")

vishal=son()
muthu=dad()
vishal.tab()
vishal.lap()
vishal.ph()
