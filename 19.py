g,s=map(int, input("number of grades and students: ").split())
l=[]

for i in range(s):
    x=list(map(float,input("grades of each student: ").split()))
    l.append(sum(x))
for i in range(len(l)):
   print(l[i]/g)



