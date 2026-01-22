2525#Question 1
num=int(input("Enter a number; I will show wheather it is Even or Odd!\n"))
num1=num%2
if(num1==0):
          print("Even")
else:
    print("Odd")



#Question 2
score=int(input("Enter your MARK! : "))
print("Score: ",score)
if(score<35):
   print("POOR STUDENT")
elif(score>=35 and score<=70):
    print("AVERAGE STUDENT")
elif(score>70 and score<100):
    print("GOOD STUDENT")
elif(score==100):
    print("EXTRODUNORY")
else:
    print("IVALID ERROR")

#Question 3 - MINI CALCULATOR
print("\nMINI CALCULATOR")
a=int(input("A: "))
b=int(input("B: "))
operation=input("ADD, SUB, DIV, MUL: ")
if(operation=="ADD"):
    print(a+b)
elif(operation=="SUB" ):
    print(a-b)
elif(operation=="DIV"):
    print(a/b)
elif(operation=="MUL"):
    print(a*b)
else:
    print("INVALID INPUT")

input("\nPress Enter for EXIT")

