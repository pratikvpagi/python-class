a=float(input("Enter first value "))
b=float(input("Enter second value"))
c=float(input("Enter third value"))

min1=a if a<b else b
min=c if c<min1 else min1
print(min)
