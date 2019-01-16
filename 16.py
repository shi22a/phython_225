s=input("The name of your company: ")

from collections import Counter
string = sorted(Counter(s).items(), key= lambda x: (-x[1],x[0]))[:3]
print("\n".join(x[0]+" "+str(x[1]) for x in string))
