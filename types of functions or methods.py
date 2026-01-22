class laptop:
    
    chargertype: "C Type"
    
    def __init__(self):      #cosntructor
        self.brand=""
        self.price=44

    def setprice(self,price):  #instance fuction
        self.price=price

    def getprice(self):         # instance function
        print("Price is ",self.price)
        
    @classmethod      #the decorator is used because class varirable does not run when there is no parameter in bracette
    def changeChargerType(cls):       # I used cls with in bractte because I called class variable that is chargertype
        cls.chargertype="B type"
        print("Chanrger type changed to", cls.chargertype)
        
    @staticmethod    #decorator,  used for just information
    def info()
    print("This is laptop class")
        

     
hp=laptop()
hp.setprice(2000)
hp.getprice()

laptop.changeChargerType()           #with our using @classmethod it will not run, because I wont type parameter inside the bracette

