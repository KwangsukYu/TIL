N = int(input())
Sublist = list(input().split())
intSublist = list(map(int, Sublist))
M = int(max(intSublist))

total = 0
for i in Sublist :
    total += int(i)/M*100

print(total/N)

