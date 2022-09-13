
def start():
    opposites=loadwords()
    word=input("Enter the word to get opposites")
    for k in opposites:
        if k == word:
            print(f"opposites of{word} is : {opposites[k]}")
        elif opposites[k]== word:
            print(f"opposites of {word} is : {opposites}")    
        else:
            w=input(f"Enter the opposite of{word}")
            addword(opposites,word,w) 
        quit=input("Quite or continue y/n")
        if quit=='y':
           break      
    saveopposites(opposites)


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


print(start())