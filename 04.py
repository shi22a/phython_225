#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

x=2000
y=3200

def find_number(a,b):
    l=[]
    for i in range(a,b):
       l.append(i)
    return l
print(find_number(x,y))


