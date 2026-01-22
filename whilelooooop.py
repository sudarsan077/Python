#while is not stopable, bt for is stoable because it use ranges

i=1
while (i<6):
    print(i)
    i=i+1
print()
i=10
while (i<201):
    print(i, end=",")
    i=i+10
print("\n")
i=10
while(i>0):
    print(i, end=",")
    i=i-1
print("\n")
i=3  
fact=1
while (i>0):
    fact=fact*i
    i=i-1
print(fact)
print()

#Madness
print("Try to stop the madness \"WHY\"")
response=""
while response != "leave me":
    response=input("Why?\n")
print("OK! I'm leaving")
