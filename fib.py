def fib(m):
    if m==0 :
        return 0
    if m==1 or m==2:
        return 1
    
    prev,curr=0,1      
    for i in range(m-1):
          prev,curr=curr,prev+curr
    return curr

num=5
i=3
for i in range(num+1):
    print(fib(i))         