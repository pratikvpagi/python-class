def count(s):
    d={}
    for letter in s:
        d[letter]=d.get(letter,0)+1
    return d

print(count("ZZaabbabccdAA"))        