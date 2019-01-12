
# factorial
num=int(input("Enter a number: "))

def factorial(n):
   f=1
   for i in range(1,n+1):
    f *=i
   return f

print("factorial (%s) = %s" % (num,factorial(num)))
