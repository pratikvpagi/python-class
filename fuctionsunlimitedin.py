# #var args
# def add(a,b,*nos):
#     print(a,b,nos)


# add(1,2)
# add(1,2,3,4,5,6)

# a,*b,c=[2,3,4,5,6,7]
# print(a,b,c)


# #key word args
# def add(a,b,*nos,**keywords):
#     print(a,b,nos)
#     print(keywords)

# add(1,2)
# add(1,2,3,4,5)
# add(2,4,3,5,name="hello",key='20')



#Function aliasing

# def foo():
#     print("foo foo")

# f=foo
# f()    

#sending a function as arg

# def foo():
#     print("foo foo")


# def bar():
#     print("bar bar")

# def caller(f):
#     f()

# caller(foo)
# caller(bar)        

# defining fuction inside the fuction
# def makeAdder(a):
#     def add(b):
#         nonlocal a   #Function closure concept
#         a+=1
#         return a+b
#     return add    

# f=makeAdder(10)
# print(f(20))    


# from audioop import reverse

# nos=["hello","bb","zzz","zaaa"]
# l=sorted(nos,key=len,reverse=True)
# print(l)


#from tkinter.tix import MAX


#marks=[{"name":"Pratik","age":20,"marks":75},{"name":"Sumit","age":19,"marks":90},{"name":"Mutturaj","age":20,"marks":100}]
# key=input("how you want to sort ? by name,age or marks")
# for i in marks:
#     for key in i:
#         if key=="name":
#             output=sorted(marks,key="name")
#             print(output)
#         elif key=="age":
#             output=sorted(marks,key="age")
#             print(output)
#         else:
#             output=sorted(marks,key="marks")
#             print(output)        


# def foo(d):
#     return d["age"]

# print(sorted(marks,key=foo))   


#lambda fuction

# print(sorted(marks,key= lambda d:d['marks']))

# property=input("Enter the basis")

# print(sorted(marks,key =lambda d:d[property]))

# print(MAX(marks,key =lambda d:d[property]))

# nos=[3,4,5,2]
# l=list(map(lambda i:i**2,nos))
# print(l)
