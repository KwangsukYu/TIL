N = int(input())
students = []
for i in range(N):
    name, korean, english, math = input().split()
    students.append((-int(korean), int(english), -int(math), name))
students.sort()
for i in students:
    print(i[3])