def readmat(size):
    mat=[]
    for i in range(size):
        row=[]
        for j in range(size):
            v=int(input(f"Enter the values for {i},{j}  "))
            row.append(v)
        mat.append(row)
    return mat        

def printmat(mat):
    for row in mat:
        print('\n')
        for c in row:
            print(c,end=" ")


def mulmat(m1,m2):
    res=[]
    for i in range(len(m1)): 
        row=[]      
        for j in range(len(m1)):
            row+=[m1[i][j]*m2[i][j]]
        res.append(row)
    return res

mat=readmat(3)
print("Now its filter")
filter=readmat(3)
m3=mulmat(mat,filter)
printmat(m3)
