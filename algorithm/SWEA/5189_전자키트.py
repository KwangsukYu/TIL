import sys
sys.stdin = open('sample_input.txt')
from itertools import permutations

def f():
    global min_v

    # 구한 모든 경우의 수를 순회하면서
    for i in range(len(a)):
        # 합을 구할 변수
        ssum = 0
        for j in range(len(a[i])):
            # 최소값보다 커지면 가지치기
            if ssum > min_v:
                break

            # 시작 지점이면 2가지를 시행
            # 1번 위치와 자기위치, 자기위치와 다음 위치의 값을 넣어줌
            if j == 0:
                ssum += arr[1][a[i][j]]
                ssum += arr[a[i][j]][a[i][j+1]]

            # 마지막 지점이면 자기위치와 1번 위치를 넣어줌
            elif j == len(a[i]) - 1:
                ssum += arr[a[i][j]][1]

            # 중간이면 자기위치와 다음위치의 값을 넣어줌
            else:
                ssum += arr[a[i][j]][a[i][j+1]]

        # 경우의 수 하나를 끝낼때마다 최소값 갱신
        if ssum < min_v:
            min_v = ssum

# 인풋 받기
for tc in range(1, 1+int(input())):
    N = int(input())

    # 인덱스 연산용으로 0 패딩 넣어주기
    arr = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    # 출발 도착지는 1이니까 1을 제외한 나머지 관리소의 경우의 수를 permutations로 구함
    A = [i for i in range(2, N+1)]
    a = list(permutations(A, N-1))
    print(a)
    min_v = 10**2*100

    # 문제 로직 함수
    f()
    print(f'#{tc} {min_v}')
