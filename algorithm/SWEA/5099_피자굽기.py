from collections import deque
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

# 인풋 받기
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    # 받은 피자의 치즈양을 피자 번호와 묶어서 리스트로 넣어줌 [치즈, 피자 번호]
    for i in range(M):
        pizza[i] = [pizza[i], i + 1]

    # 화덕 크기만큼 [0, 0] 을 넣어준다 > while문을 돌리기 위해서
    box = deque()
    for i in range(N):
        box.append([0, 0])

    # 화덕에 피자 하나가 남아있을 경우
    while len(box) > 1:

        # 화덕의 가장 첫번째 피자를 뽑아서
        v = box.popleft()

        # 치즈양 // 2 를 해주고
        c = v[0] // 2

        # 그게 0 이면 꺼내고 다른 피자를 순서대로 넣어준다. 없으면 except로 처리
        if c == 0:
            try:
                box.append(pizza.pop(0))
            except:
                pass

        # 치즈가 남아있다면 치즈양을 반으로 줄이고 다시 화덕에 추가
        else:
            v[0] = c
            box.append(v)

    # 남은 화덕엔 피자가 1개이므로 그 피자의 번호를 출력력
    print(f'#{tc} {box[0][1]}')




