from collections import deque
import sys
sys.stdin = open('input (1).txt')

# 연산자가 문자열로 들어와서 연산자마다 계산 할 함수
def cal(o, n1, n2):
    if o == '+':
        return n1 + n2
    if o == '-':
        return n1 - n2
    if o == '/':
        return n1 / n2
    if o == '*':
        return n1 * n2
# 후위 순회로 돌면 계산식이 편하게 나와서 연산자와 숫자를 구별해서 넣어주기
def check(s):
    if s:
        check(ch1[s])
        check(ch2[s])
        if v[s]:
            q.append(v[s])
        if num[s]:
            q.append(num[s])

# 연산자, 정점 값, 인덱스로 만들 자식 트리
for tc in range(1, 11):
    V = int(input())
    v = [0] * (V + 1)
    num = [0] * (V + 1)
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)

    # 각각 4개일 때 2개일 때 나누어서 넣어줌
    for i in range(V):
        input_v = input().split()

        if len(input_v) == 4:
            v[int(input_v[0])] = input_v[1]
            ch1[int(input_v[0])] = int(input_v[2])
            ch2[int(input_v[0])] = int(input_v[3])

        else:
            num[int(input_v[0])] = int(input_v[1])

    # q는 덱으로 설정하고
    q = deque()

    # 위 함수를 실행하면
    check(1)

    # q에 계산하기 이쁘게 담긴다.
    # print(q)
    # deque([88, 65, '-', 10, '-'])

    stack = [q.popleft()]

    # stack을 활용해서 숫자면 녛어주고 연산자면 숫자 2개를 빼서 연산을 진행
    while q:
        v = q.popleft()

        try:
            if int(v):
                stack.append(v)
        except:
            v1 = stack.pop()
            v2 = stack.pop()

            # eval 함수를 써보고 싶었는데 swea에서 지원을 하지 않는다.
            # stack.append(eval(f'{v2}{v}{v1}'))
            stack.append(cal(v, v2, v1))


    print(f'#{tc} {int(stack[0])}')