def painter():
    print("Printing")
painter()
print()
print("1. MINI CALCI")
def add():
    c=a+b
    print("Addtion is : ",c)
def sub():
    c=a-b
    print("Subraction is : ",c)
def mul():
    c=a*b
    print("Multiplication: ",c)
def div():
    if (b!=0):
        c=a/b
        print("Divition is: ",c)
    else:
        print("ERROR: Cannot divide by Zero")
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
call=input("add, sub, mul, div"+": ")
if (call=="add"):
    add()
elif (call=="sub"):
    sub()
elif (call=="mul"):
    mul()
elif (call=="div"):
    div()
else:
    print("Invalid code")
print()

def painter(msg):
    print("Message is: ", msg)
painter("paint my house")
print()

print("2. EVEN or ODD")
def eveorodd():
    if(a%2==0):
        print("The Entered number is EVEN")
    else:
        print("The Entered number is ODD")
a=int(input("Enter the number: "))
eveorodd()
print()

print("3. Print Range")
def rangee():
    print("The numbers are: ",end=""
          )
    for i in range (a,b+1):
        print(i,end=",")
print("Enter the two number I'll print the range for you")
a=int(input("A: "))
b=int(input("B: "))
rangee()


