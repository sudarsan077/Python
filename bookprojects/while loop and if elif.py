username=""
while not username:
    username=input("Username: ")
    if (username==""):
        print("User should not be empty")
        print()

password=""
while not password:
    password=input("Password: ")
    if password=="":
        print("pass should not be empty")

if username=="mssusan077" and password=="9025":
    print("Access Granted")
elif username=="vish2005" and password=="2005":
    print("Access Granted")
else:
    print("Incorrect Credentials")
print()
#_______________________________________------
print("Lets play a game, I think a random number between 1 to 10")
print("Let you guess the number I think with in five attempts")
print("Lets, GOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!")
import random
number=random.randint(1,10)
guess=int(input("Enter you guess: "))
tries=1
while guess!=number:
    if guess>number:
        print("Lesser..")
    else:
        print("Greater..")

    guess=int(input("Lets take a try: "))
    tries+=1
    if tries==5 and guess!=number:
        print("Game Over, there is no attempt")
        print("The number is ",number)
        break
print()
if guess==number:
    print("You Guessed it!!, the number was",number)
    print("You took only\"",tries,"\"tries")
        

