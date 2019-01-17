n=input("Enter a number: ")
r=input("Enter a list of rooms: ")

rr=map(int, r.split())
rooms=[]
caproom=[]

for i in rr:
    if i not in rooms:
        rooms.append(i)
    else:
        caproom.append(i)
print(list(set(rooms)-set(caproom)))