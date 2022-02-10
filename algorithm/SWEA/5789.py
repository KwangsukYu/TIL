import sys
sys.stdin = open('sample_input.txt')

# 첫 상자는 모두 0
# Q회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경
# i번째 (1 <= i <= Q) 작업에 대해 L부터 R까지 i로 변경 첫번째 작업 = 1 두번째 = 2
# Q회 동안의 작업을 순서대로하고 N개의 상자에 적힌 값을 순서대로 나열
# 각 케이스마다 Q회 반복!

T = int(input())
for ts in range(1, T + 1):
    N, Q = map(int, input().split())
    boxes = [0] * N
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L - 1, R):
            boxes[j] = i
    print(f'#{ts}', *boxes)





