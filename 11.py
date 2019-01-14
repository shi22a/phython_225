

x="Krishna 67 68 69"
y="Arjun 70 98 63"
z="Malika 52 56 60"

def mean(l):
    stus = {}
    for i in range(0, len(l)):
        name, math, physic, chemistry = l.split(" ")
        stus[name] = (float(math) + float(physic) + float(chemistry)) / 3
        if name in stus:
            return (name,"%.2f" % stus[name])
        else:
            return ("No")

print(mean(x))
print(mean(y))
print(mean(z))
print(max(mean(x)[1],mean(y)[1],mean(z)[1]))


