# 첫 학생은 무조건 0번을 뽑고 가장 처음
# 두번 째 학생은 0과 1, 0을 뽑으면 그자리, 1번 뽑으면 바로 앞의 학생 앞
# 세번 째 0, 1, 2 뽑은 번호만큼 앞자리로
N = int(input())
ans = []
number = list(map(int, input().split()))

for i in range(1, N + 1):
    ans.append(i)
    if number[i-1] == 0:
        continue
    else:
        for j in range(1, number[i-1]+1):
            ans[i-j], ans[i-1-j] = ans[i-1-j], ans[i-j]
print(*ans)