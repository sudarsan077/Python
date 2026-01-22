def painter():
    return "Hello! Brother"
msg=painter()
print(msg)
print()

print("ID PASS LOGIN")
username_s="mssusan"
pass_s="Susan@123"
username=input("Username: ")
pasw=input("Password: ")
def security():
    if(pass_s==pasw and username==username_s):
        return True
    else:
        return False
sec=security()
print(sec)
print()

print("ADDITION and MULTI")
a=int(input("A: "))
b=int(input("B: "))
c=int(input("c: "))
def add(n1,n2):
    return n1+n2
adtn=add(a,c)
def mul(n3):
    return adtn*n3
mlti=mul(b)
print("Addition of first two number is: ",adtn)
print("Multiplication of added value is: ",mlti)
