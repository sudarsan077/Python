#Question 1
print("Type two numbers I will print; the number that are between in which the number you entered")
a=int(input("Enter number one: "))
b=int(input("Enter second number: "))
for c in range(a+1,b):
    print(c)
print()

#Question 2
print("Enter two numbers I will print Even numbers between the number you entered")
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
count=0 #to count howmany evens in the inpueted range
for c in range(a,b):
    if(c%2==0):
        print(c)
        count=count+1
print("The total even numbers are: ",count)
print()

#Question 3
print("Enter two number I'll show the count of number of odd and even numbers between them..")
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
counteven=0
countodd=0
for i in range(n1,n2):
    if(i%2==0):
        counteven=counteven+1
    else:
        countodd=countodd+1
print("Total even numbers are: ",counteven)
print("Total odd numbers are: ",countodd)

