


s="Hello Word"

def up_letter(x):
    l=[]
    for i in x:
        if  97 <= ord(i) <= 122:
            l.append(x.upper())
            return l
print("".join(up_letter(s)))


