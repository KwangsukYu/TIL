N = int(input())
stack = []
ans = []
num = 1
for i in range(N):
    n = int(input())

    while num <= n:            # 인풋 값으 수만큼 push 해줌
        stack.append(num)      # stack에는 숫자
        ans.append('+')        # ans에 기호
        num += 1               # 숫자에 +1 해줌

    if stack[-1] == n:         # 만약 stack의 top이 숫자랑 같으면
        stack.pop()            # pop을 해주고
        ans.append('-')        # 기호에 - 추가
    else:
        ans = ['NO']           # 아니면 NO하고 break로 탈출
        break

print('\n'.join(ans))          # 형식에 맞게 출력

