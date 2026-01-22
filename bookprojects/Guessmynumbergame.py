import random

def dies():
    ingo=input("Type \"Go\" to roll the dies  ")
    if (ingo=="go"):
        dies1=random.randint(1,6)
        dies2=random.randrange(7)

        total=dies1+dies2

        print("you rolled a",dies1,"and a",dies2,"for a total of",total)
    else:
        print("OOOOOOOOOOOOOOOPPPPPPPPPSSSSSSSSSSSS!!!!!!!!!!!!!")
        print("""
                --------
               |        |
               |  0  0  |
               |   <    |
               |   0    |
               |________|""")
dies()

