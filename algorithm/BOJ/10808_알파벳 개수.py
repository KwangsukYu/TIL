T = input()
ans = [0] * 26
for i in T:
    ans[ord(i)-97] += 1

print(*ans)