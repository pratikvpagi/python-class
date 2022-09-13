start = int(input("enter the start value\n"))
end = int(input("enter the end value\n"))

# while start < end:
#     if start % 2 == 0:
#         print(start)
#         # break
#     start += 1
# else:
#     print("i am here")

# while True:
# while True:
#     if start > end:
#         break

#     if start%2 == 0:
#         print(start)
    
#     start += 1
# else:
#     print("i am here")

while start <= end:

    if start%2:
        start += 1
        continue
    
    print(start)
    start += 1

else:
    print("i am here")
