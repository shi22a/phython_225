import math
k=3
m=1000
n=[]
f=[]
for i in range(k):
    n.append(max(list(map(int, input().split()))))
for j in n:
    f.append(j**2)
print(sum(f)%1000)