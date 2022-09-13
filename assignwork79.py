print("D:Devil,T=Treasure,P=Person")
s=(
'____________________'
'\n|         |         |'
'\n|   D     |    T    |'
'\n|_________|_________|'
'\n|         |         |'
'\n|         |    P    |'
'\n|_________|_________|'
)

print(s)
print("Instuctions for playing \n U=UP \n D=Down \n R=Right\n L=Left ")
choice=(input("Enter the character as per instructions :"))
if choice=='U':
    print("win")
elif choice=='L':
    print("!empty")
    print   (
'____________________'
'\n|         |         |'
'\n|   D     |    T    |'
'\n|_________|_________|'
'\n|         |         |'
'\n|    P    |         |'
'\n|_________|_________|'
)  
    print("Move again by entering char as per instructions")
    choice2=(input())   
    if choice2=='U':
       print("DEVIL KILLED YOU!!! ")
       print(
'____________________'
'\n|         |         |'
'\n|   D     |    T    |'
'\n|_________|_________|'
'\n|         |         |'
'\n|         |         |'
'\n|_________|_________|'
)  
    else:
        print("same place")       
elif choice=='D':
    print("can't move no space")
    print("defeat")       