# N 학생수 K 방 최대 인원수 S 0 여학생 1 남학생 Y학년

N, K = map(int, input().split())
man = [0]*6
woman = [0]*6
for ts in range(N):
    S, Y = map(int, input().split())
    if S:
        man[Y-1] += 1
    else:
        woman[Y-1] += 1
ans = 0

for i in man:
    if i % K != 0:
        ans += i // K + 1
    else:
        ans += i // K 

for i in woman:
    if i % K != 0:
        ans += i//K + 1
    else:
        ans += i//K 

print(ans)




