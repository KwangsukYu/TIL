import sys
sys.stdin = open('input.txt')

# 접근 방법
# 어차피 교착 상태가 되는 것은 1과 다음에 나오는 2
# 이거 두개의 갯수만 구해주면됨, 괄호랑 비슷하게

for tc in range(1, 11):
    N = int(input())
    arr_r = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    arr = []

    # 세로줄로만들고 0을 제외한 숫자값을 리스트로 다시 만듬
    # 바로 구해도 가능하나 직관적으로 보면서 하기 편함
    for i in list(map(list, zip(*arr_r))):
        empty = []
        for j in i:
            if j != 0:
                empty.append(j)
        arr.append(empty)

    # 구간을 반복하며 1일때 다음에 오는게 2인지 확인하고
    # cnt에 추가해줌
    for i in range(len(arr)):
        for j in range(len(arr[i]) - 1):
            if arr[i][j] == 1:
                if arr[i][j+1] == 2:
                    cnt += 1

    print(f'#{tc} {cnt}')



