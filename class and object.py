class goa:
    name=""
    drink=""
    def party(self):
        print("Lets party!")
    def travel(self):
        print("Tavel")
        
ramesh=goa()
suresh=goa()

ramesh.name="Ramesh"
suresh.name="Suresh"

ramesh.drink="Yes"
suresh.drink="No"

print(ramesh.name)
print("Drink: ",ramesh.drink)
print(suresh.name)
print("Drink: ",suresh.drink)

ramesh.party()
suresh.travel()
print()
#------------------------------------------------------------
class laptop:
    price=0
    processor=""
    ram=""
hp=laptop()
dell=laptop()

hp.price=50000
hp.procc="i5"
hp.ram="8 gb"

dell.price=60000
dell.procc="i7"
dell.ram="10 gb"

print(dell.procc)
        


