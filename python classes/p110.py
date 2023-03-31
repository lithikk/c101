import random
response=input("Press y to roll again or press n to exit")
respone='y'
while response == "y":
    no = random.randint(1,6)
    if no==1:
        print("The number on the dice is 1")
        
    if no==2:
        print("The number on the dice is 2")

    if no==3:
        print("The number on the dice is 3")

    if no==4:
        print("The number on the dice is 4")

    if no==5:
        print("The number on the dice is 5")

    if no==6:
        print("The number on the dice is 6")
    print("\n")
       

