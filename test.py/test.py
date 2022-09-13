c=40

lw=0
nc=0
remainde=0
while lw==0:
    w=c
    lw=w//2
    c+=lw
    nc=lw//2
    remainde=w-lw
    c+=nc
    lw+=remainde*2

print(c)    
