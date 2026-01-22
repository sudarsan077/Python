#instance variable
class mobile:
    def __init__(self,model,strg,battery):
        self.model=model
        self.strg=strg
        self.battery=battery
    def display(self):
        print("Model: ",self.model)
        print("Storage: ",self.strg)
        print("Battery Capacity: ",self.battery)
        
vivo=mobile("v40e","128GB","4000mah")
oppo=mobile("Reno 3","258 GB","5000 mah")
realme=mobile("GT 6T","512 GB","6000 mah")

vivo.display()
oppo.display()
realme.display
#--------------------------------------------------------
#class variable- used if a particular variable has same for all objects
class bike:
    cc="350"
    def __init__(self,model,milage):
        self.model=model
        self.milage=milage
    def display(self):
        print("Model: ",self.model)
        print("Milage: ",self.milage)
        print("CC: ",self.cc)

re=bike("Clssic reborn","32")
honda=bike("Hyness","33")
jawa=bike("Perak","30")

re.display()
honda.display()
jawa
.display()

        
