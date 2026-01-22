#Question 1
print("Fibonanccy series")
sum=0
for nn in range (1,6):
    sum=sum+nn  #sum is same like count, in count we add number one. but, in sum we add the variable (nn)
print(sum)
print()
#--------------------------------------------------------------------------------------------------------------------------------------

#LIST[]
print("LIST BASIC")
a=[1,2,3,4,5] #collection of data is called list
for i in a:
    print(i)
print()
#----------------------------------------------------------------------------------------------------------------------------------------
#OWN Solving
#Q2 - get ten input from user, add it and average it 
word="Enter No "
sum=0
for ui in range (1,11):  #user input(ui)
    print(word,ui)
    add=int(input())
    sum=sum+add
avg=sum/10
print("TOTAL :",sum)
print("AVERAGE:",avg)
print()

#Q2 - Get wten input from user, add it and average it
# youtube code; important concept - APPEND
a=[]
print("Enter Ten Numbers")
for i in range(1,11):
    num=int(input("Enter number " + str(i) + ": "))             # + is used to join words, so i the integer is converted as string this is called casting 
    a.append(num)                                             #append: the number we enter in (num) is stored in (a=[]) list
print(a)
sum=0
for i in a:
    sum=sum+i
print("TOTAL: ",sum)
print("AVEAGE: ",sum/10)
print()
#------------------------------------------------------------------------------------------------------------------------------------------------------------


























