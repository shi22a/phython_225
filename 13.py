from collections import namedtuple

N = int(input("Enter a number of student: "))
fields = input("Enter fields: ").split()

total = 0
for i in range(N):
    students = namedtuple('student',fields)
    field1, field2 = input("Enter name and grade: ").split()
    student = students(field1,field2)
    total += int(student.grade)
print('{:.2f}'.format(total/N))



