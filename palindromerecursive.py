def palindrome(s):
    if not s:
        return True
    return s[0]==s[-1] and palindrome(s[1:-1])

print("Palindrome"if palindrome("a"*2000) else "Not palindrome")        