N = int(input())
lst = [0] * 26

for i in range(N):
    t = input()
    lst[ord(t[0])-97] += 1

flag = False
for i in range(26):
    if lst[i] >= 5:
        print(chr(i+97), end='')
        flag = True

if not flag:
    print('PREDAJA')