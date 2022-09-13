import random
print("okay keep a number in your mind")
limit=5
num=(random.randint(0,limit))
newnum=num
for x in range(limit):
    print("is it",newnum)
    choice=input("Enter input 'y' for correct and ge for greter and le for lesser")

    if choice=='y':
        print("i guessed it!")
        break

    elif choice=='le':
        newnum-=1
        print("is it",newnum)    
    
    elif choice=='ge':
        newnum+=1
        print("is it",newnum) 
    
    else:
        continue           
        