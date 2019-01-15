import math

AB=int(input("length AB= "))
BC=int(input("length BC= "))

AC=(AB**2+BC**2)**(1/2)
ab=math.asin(AB*math.sin((90* math.pi / 180))/AC)
print(ab*180/math.pi )
