import sys

sys.stdin = open('input (3).txt')

for tc in range(1, 11):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    m_x = m_y = c_x = c_y = 0

    for i in range(100):
        x = y = 0
        for j in range(100):
            x += arr[i][j]
            y += arr[j][i]
            if i == j:
                c_x += arr[i][j]
                c_y += arr[i][-j-1]
        if m_x <= x: m_x = x
        if m_y <= y: m_y = y
    ans = 0
    ans_li = [m_x, m_y, c_x, c_y]
    for i in ans_li:
        if i >= ans:
            ans = i
    print(f'#{tc} {ans}')
