words={"good":"bad","white":"black","up":"down"}
newword={}
uw=input("enter your word")
def oppo(w):
    for i in words:
        if i == uw:
            return words[i] 
        elif words[i]==uw:
            return i    
    else:
         print("i dont have\n")
         newword=words
         newword.update(i=input("input the opposite"))
    print(newword)

print(oppo(uw))