#loop string
word=input("Enter any word\n")
for letter in word:
    print(letter)
print()

#counter
print("Counting")
for i in range(1,11):
    print(i,end=" ")
print("\n\nCounting by fives")
for j in range(0,51,5):
    print(j,end=" ")
print("\n\nCounting backward")
for k in range(10,0,-1):
    print(k, end=" ")

#length
msg=input("\n\nEnter the message\n")
print("The length of the message is ",len(msg))
    
