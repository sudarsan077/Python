#basic usual program
def add(a,b,c):
    print(a+b)

add(2,8,5)
print()

#polymorphism
print("using Poly")
def add(a,b,c=0):  #c=0, this is polymorphism 
    print(a+b+c)

add(5,5)     #using c=0 we can do input for only a and b
add(5,5,3)  # eventhough c=0, the value we enter for c here is considered, so this poly.

#practice------------------------------------------------------
print()
print("practice")

class animal():
    def sound(self):
        print("Animal makes a sound")
class dog(animal):  #inherits animal class
    def sound(self):
        print("Dog barkes")
class bird(dog):     #inherites both dog and animals class
    def sound(self):
        print("Bird sings")

bairav=dog()
kuyil=bird()
bairav.sound()     #eventhough dog class inherites animal class it print its own sound function(Note: all functions are named as "sound")
kuyil.sound()       #eventhough bird clss inherites both dog and animal cls it prints its own sound function as "Bird sings"
