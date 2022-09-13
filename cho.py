def chocolatefeast(n,c,m):
    bars=n//c
    w=bars
    while(w>=m):
        bars+=w//m
        w=w//m+w%m
    return bars

print(chocolatefeast(2,1,40))