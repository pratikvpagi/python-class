a = [1,2,4,3.4,"hello",[2,3,4]]
a[0]=1000
print(a[0])
print(a[1])
print(a[-1])
print(len(a))
print(a[-1][0])
c = a+[22,33]
print(c)
d = a[:]
d[-1][0]=200
print(a)

def sq(nos):
    # res = [] 
    # for num in nos:
    #     res += [num**2]
    # return res
    return [num**2 for num in nos]

print(sq([2,3,4,5]))