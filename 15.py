

from collections import OrderedDict

dict = OrderedDict()
for i in range(int("4")):
    key = input("word: ")
    if not key in dict.keys():
        dict.update({key : 1})
    elif key in dict.keys():
       dict[key] += 1

print(len(dict.keys()))
print(*dict.values())
