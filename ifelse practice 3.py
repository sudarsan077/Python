#Question 1
print("Let check your loan eligible criteria")
print("Are you salaried?")
choice=input("Yes,No: ")
if(choice=="Yes"):
    limit=int(input("Enter your Salary per month: "))
    if(limit>=20000):
        print("You are eligible!!!")
        amount=int(input("Enter your loan amount: "))
        if(amount<=50000):
            print("Loan sactation could be considered.  Our team will soon contact you.\nTHANKING YOU.")
        else:
            print("Current the amount is not available.\nSORRY FOR INCONVENIENCE.")
    else:
        print("You are Not Eligible.")
else:
    print("Sorry, You are not eligible")
print("\n")

#Question 2
print("Enter your Marks.")
eng=int(input("English: "))
tam=int(input("Tamil: "))
mat=int(input("Maths: "))
sci=int(input("Science: "))
soc=int(input("Social: "))
total=eng+tam+mat+sci+soc
avg=total/5
print("Your Total: ",total,"/500")
if(tam>=35 and eng>=35 and mat>=35 and sci>=35 and soc>=35):
    print("Your Average: ",avg)
    print("You are good to goo!")
elif(avg<35):
    print("Must have to push for better marks!")
elif(tam<35):
    print("Special class needed for \"TAMIL\"")
elif(eng<35):
    print("Special class needed for \"ENGLISH\"")
elif(mat<35):
    print("Special class needed for \"MATHS\"")
elif(sci<35):
    print("Special class needed for \"SCIENCE\"")
elif(soc<35):
    print("Special class need for \"SOCIAL\"")
else:
    print("You are good to go")

