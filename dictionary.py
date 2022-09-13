# ^C
# (base) C:\Users\prati\python-class>python palindromerecursive.py
# Palindrome

# (base) C:\Users\prati\python-class>python palindromerecursive.py

# Palindrome

# (base) C:\Users\prati\python-class>python
# Python 3.9.12 (main, Apr  4 2022, 05:22:27) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> d={1:'hello',2:'hi,"pratik":"Mutturaj"}
#   File "<stdin>", line 1
#     d={1:'hello',2:'hi,"pratik":"Mutturaj"}
#                                            ^
# SyntaxError: EOL while scanning string literal
# >>> d={1:'hello',2:'hi,"pratik":"Mutturaj"} type(d)
#   File "<stdin>", line 1
#     d={1:'hello',2:'hi,"pratik":"Mutturaj"} type(d)
#                                                    ^
# SyntaxError: EOL while scanning string literal
# >>> d={1:'hello',2:'hi',"pratik":"Mutturaj"}
# >>> type(d)
# <class 'dict'>
# >>> len(d)
# 3
# >>> for k in d:
# ... print(k)
#   File "<stdin>", line 2
#     print(k)
#     ^
# IndentationError: expected an indented block
# >>> for k in d:
# ...    print(k)
# ...
# 1
# 2
# pratik
# >>> for i in d:
# ...    print(d[i])
# ...
# hello
# hi
# Mutturaj
# >>> d['hello']='hi'
# >>> print(d)
# {1: 'hello', 2: 'hi', 'pratik': 'Mutturaj', 'hello': 'hi'}
# >>> d[1]='hi'
# >>> print(d)
# {1: 'hi', 2: 'hi', 'pratik': 'Mutturaj', 'hello': 'hi'}
# >>> d.pop("hello")
# 'hi'
# >>> print(d)
# {1: 'hi', 2: 'hi', 'pratik': 'Mutturaj'}
# >>> for i in d:
# ...   print(i,"-->",d[i])
# ...
# 1 --> hi
# 2 --> hi
# pratik --> Mutturaj

# d={1:'hello',2:'hi',3:'name'}


# d={1:0,2:1}
# def fib(n):
#     if n in d:
#         return d[n]
#     d[n]=fib(n-1)+fib(n-2)
#     return d[n]

# print(fib(1000))
from logging import exception


d={1:0,2:1}
def fib(n):
    try:
        return d[n]
    except Exception as e:
        d[n]=fib(n-1)+fib(n-2)
        return d[n]

print(fib(1000))        