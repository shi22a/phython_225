#Write a program that accepts sequence of lines as input
# and prints the lines after making all characters in the sentence capitalized.


s=input("Enter a sentence: ")

def up_letter(x):
    l=[]
    for i in x:
        if  97 <= ord(i) <= 122:
            l.append(x.upper())
            return l
print("".join(up_letter(s)))


