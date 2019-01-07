def recurse(n):
    if n<=0:
        print("Thing!")
    else:
        print(n)
        recurse(n-1)
        print(n)

recurse(4)

string = 'hello'
string.isupper()
string.upper()
