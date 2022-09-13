string=input("Enter a word")
letter=input("Enter the letter you want to replace")

substring=string[1:len(string)-1]
s = letter+substring+letter
print(s)
