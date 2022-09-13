n=int(input("Enter number"))
range=int(input("Enter range"))
count=1
while count<=range:
    prod=n*count
    print(f"{n}x{count:>5}={prod:<10}")
    count+=1