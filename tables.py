n=int(input("Enter number"))
range=int(input("Enter range"))
count=1
while count<=range:
    prod=n*count
    print(n,'x',count,'=',prod)
    count+=1