N = int(input())

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
ans1 = 0
ans2 = 0
for i in range(N):
    if lst1[i] in lst2:
        if lst1[i] == lst2[i]:
            ans1 += 1
        else:
            ans2 += 1

print(ans1)
print(ans2)