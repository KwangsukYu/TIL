N = int(input())
lst = []

for i in range(1,30000000):
    if '666' in str(i):
        lst.append(i)
print(lst[N-1])