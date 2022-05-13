N = int(input())
lst = []
for i in range(N):
    age, name = input().split()
    lst.append((int(age), i, name))

lst.sort()

for i in lst:
    print(i[0], i[2])