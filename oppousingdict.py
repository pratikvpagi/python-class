
# words={"good":"bad","white":"black","up":"down"}
# newword={}
# uw=input("enter your word")
# def oppo(w):
#     for i in words:
#         if i == uw:
#             return words[i] 
#         elif words[i]==uw:
#             return i    
#     else:
#          print("i dont have\n")
#          newword=words
#          newword.update(i=input("input the opposite"))
#     print(newword)

# print(oppo(uw))

import pickle
def loadwords():
    try:
        f=open("words.pkl","rb")
        opposites=pickle.load(f)
    except Exception as e:
        opposites={"up":"down","sit":"stand"}
    return opposites


def saveopposites(words):
    try:
        f=open("words.pickle","wb")
        pickle.dump(words,f)
        f.close
    except Exception as e:
      print(e)
      print("unable to write")

def addword(opposite,word,opp):
    opposite[word]=opp

# def start():
#     opposites=loadwords()
#     for word in opposites:
#         word=input("Enter the word to get opposites")
#         if word in opposites:
#             print(f"opposites of{word}is {opposites[word]}")
#         elif word == opposites[word]:
#             print(f"opposites of {word}is {opposites}")    
#         else:
#             w=input("Enter the opposite of{word}")
#             addword(opposites,word,w) 
#         quit=input("Quite or continue y/n")
#         if quit=='y':
#             break       
#     saveopposites(opposites)


def start():
    opposites=loadwords()
    while True:
        word=input("Enter the word to get opposites")
        opp=getopposite(opposites,word)
        if opp:
            print(f"opposite of {word} is {opp}")
        else:
            w=input(f"Enter the opposite of{word}")
            addword(opposites,word,w) 
            quit=input("Quite or continue y/n")
            if quit=='y':
                break       
    saveopposites(opposites)

def getopposite(opposites,word):
    for k in opposites:
        if k==word:
            return opposites[k]
        elif opposites[k]==word:
            return k
    return " "             


print(start())
