#Question1
mark=int(input("Q1:  Enter you mark socred for hundred: "))
if(mark>35):
    print("Passed")
else:
    print("Failed")
print() #line space

#Question 2
salary=int(input("Q2:  Your Salary?:"))
if(salary<7000):
    print("You are eligible for scholarship")
else:
    print("You are not eligible for scholarship")
print()

#In division to find quotionte we use (/) to find remainder we use(%)
print("15 div by 5; Quotionte is: ",15/5)
print("15 div by 5; Remainder is: ",15%5)
print()

#Question 3
a=int(input("Enter a number I'll show which is divisible by 3 and 5: "))
f3=a%3
f5=a%5
if(f3==0 and f5==0):   #Binary operators : and, or, not
    print("The number is divisible")
else:
    print("The number is not divisible")

input("\nPress enter to Exit")



