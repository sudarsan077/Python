class laptop:
    def __init__(self):   #inbuild python's function which is call itself automatically without we call it this is called constructor
        self.ram=""
        self.processor=""
    def dis(self):
        print("ram: ",self.ram)
        print("processor: ",self.processor)

hp=laptop()
dell=laptop()

hp.ram="8gb"
hp.processor="i5"

dell.ram="10 gb"
dell.processor="i7"

dell.dis()
hp.dis()
