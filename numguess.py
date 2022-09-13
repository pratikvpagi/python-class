import random 
compnum=random.randint(0,10)


while True:
    usernum=int(input("guess the number"))
    if usernum==compnum:
        print("correct guess")
        break
    elif usernum<compnum:
        print("give greater num  ")
    elif usernum>compnum:
        print("give lesser number")
    else:
        use=usernum