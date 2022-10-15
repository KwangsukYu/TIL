import sys
sys.stdin = open('sample_input.txt')

# 맨 왼쪽이 아니면 현재 6번과 왼쪽 2번 비교
def leftside(num, d):
    global spin
    
    if num:
        if arr[num][6] != arr[num-1][2]:
            spin[num-1] = -1 * d
            leftside(num-1, -1 * d)

# 맨 오른쪽이 아니면 현재 2번과 오른쪽 6번 비교
def rightside(num, d):
    global spin

    if num < 3:
        if arr[num][2] != arr[num+1][6]:
            spin[num+1] = -1 * d
            rightside(num+1, -1 * d)

# 배열 변경하기
def spin_arr(num, spin):
    global arr
    if spin < 0:
        x = arr[num].pop(0)
        arr[num].append(x)
    elif spin > 0:
        x = arr[num].pop()
        arr[num].insert(0, x)
    else:
        return

T = int(input())

for tc in range(1, T+1):
    k = int(input())
    arr = [list(map(int, input().split())) for _ in range(4)]

    for _ in range(k):
        spin = [0, 0, 0, 0]                            # 각 자석이 어떻게 회전하는지, 1 = 시계, -1 = 반 시계
        num, dist = map(int, input().split())          # 인풋 값 받기
        num -= 1                                       # 1 빼주고 계산하기
        spin[num] = dist                               # 인풋 값은 spin에 바로 넣어주기
        leftside(num, dist)                            # 왼쪽편 회전 구하기
        rightside(num, dist)                           # 오른쪽편 회전 구하기
        for i in range(4):                             # spin값을 기준으로 배열 변경해주기
            spin_arr(i, spin[i])

    ans = 0                                            # 정답구하기, 2의 제곱수
    for i in range(4):
        if arr[i][0]:
            ans += 2**i
    
    print(f"#{tc} {ans}")