a=[]
sum=0
for i in range (1,5):
    num=int(input("Enter number "+str(i)+": "))
    a.append(num)
for i in a :
    sum=sum+i
print(a)
print("TOTAL: ",sum)
print()
i=5
fact=1
while (i>0):
    fact=fact*i
    i=i-1
print(fact)
