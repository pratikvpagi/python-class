letter=input("Enter a letter ")
alphabet= 'a'<=letter<='z' or 'A'<=letter<='Z'
digit= '0'<=letter<='9'
vowel=letter in'aeiouAEIOU'

if alphabet:
    print(alphabet)
    print('vowel' if vowel else 'consonant')
elif digit:
    print(f"{letter} is a digit")
else:
    print("special")    

