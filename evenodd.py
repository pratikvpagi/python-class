num=int(input("Enter number"))
print(num)
'''
if num%2==0:
    print("number is even")
else:
    print("number is odd")    
'''
'''temp =num
ldigit =temp//10

if ldigit%2:
    print("the number is even")
else:
    print("the number is odd") 
print(ldigit)
'''
'''
r=2*(num//2)-num
print("even" if r==0 else "odd")
'''
evens='02468'
odd='13579'
last_digit=num-10*(num//10)
print(last_digit)
print("even" if str(last_digit) in evens else "odd")