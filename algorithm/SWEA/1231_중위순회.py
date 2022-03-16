import sys
sys.stdin = open('input.txt')

# 중위 순회 함수
def in_order(V):
    if v[V]:
        in_order(ch1[V])
        print(v[V], end='')
        in_order(ch2[V])

# v에는 문자열을, ch1과 ch2에는 각각 왼쪽, 오른쪽 자식을 넣을 리스트 만들기
for tc in range(1, 11):
    V = int(input())
    v = [0] * (V + 1)
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)

    # 변수 하나로 받아서 그 길이가 2, 3, 4일 때를 나누어 각각 알맞게 만들어둔 리스트에 넣어줌
    for i in range(V):
        input_v = input().split()

        if len(input_v) == 4:
            v[int(input_v[0])] = input_v[1]
            ch1[int(input_v[0])] = int(input_v[2])
            ch2[int(input_v[0])] = int(input_v[3])

        elif len(input_v) == 3:
            v[int(input_v[0])] = input_v[1]
            ch1[int(input_v[0])] = int(input_v[2])

        else:
            v[int(input_v[0])] = input_v[1]

    # 출력 형식을 맞추기 위한 부분
    print(f'#{tc}',end=' ')
    in_order(1)
    print()

