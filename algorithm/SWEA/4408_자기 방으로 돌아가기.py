import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    room = [0 for i in range(200)]
    N = int(input())
    for _ in range(N):
        now, back = map(int, input().split())

        start = 0
        if now % 2:
            start = now//2
        else:
            start = now//2 - 1

        end = 0
        if back % 2:
            end = back//2
        else:
            end = back//2 - 1

        if start > end:
            start, end = end, start

        for i in range(len(room[start:end+1])):
            if room[start+i] == 1:
                room[start+i] = -1
            elif room[start+i] == 0:
                room[start + i] = 1
            else:
                room[start + i] -= 1

    min_v = 0
    ans = 1
    for i in room:
        if i < 0:
            if min_v > i:
                min_v = i
        elif i >= 0:
            ans += min_v * -1
            min_v = 0
    else:
        ans += min_v * -1

    print(f'#{tc} {ans}')

