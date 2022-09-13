import random
word_list=["Hello","engineering","Lucid","Dream","soulprojection"]
hangman=("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")

word=random.choice(word_list)
print("_"*len(word))

def lettercorrect(l):
    for i in range(len(word)):
        if l==word[i]:
            print(l[i])

l=input("Enter your letter")
lettercorrect(l)       