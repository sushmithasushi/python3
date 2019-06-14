import string
def abc(string):
    s1="abcdefghijklmnopqrstuvwxyz"
    for d1 in s1:
        if d1 not in string.lower():
            return False
    return True
string=input()
if (abc(string)==True):
    print("yes")
else:
    print("no")
