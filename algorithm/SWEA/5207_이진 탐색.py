import sys
sys.stdin = open('sample_input.txt')

# target, start, end, direction 을 인자로 받아서 함수 실행
def search(num, l, r, direction):
    global cnt

    # 탐색이 끝나면 종료
    if l > r:
        return

    # 중간 값 설정
    m = (l + r)//2

    #만약 중간값과 target이 일치하면 cnt에 추가(밑의 분기에서 번갈아가지 못했으면 자동으로 종료가 됨)
    if num == A[m]:
        cnt += 1
        return

    # 문제의 조건에서 탐색을 번갈아가면서 진행해야 하므로 왼쪽 일 땐 오른 쪽 반대 쪽도 마찬가지로 조건을 설정
    # 처음 방향은 모르니 방향을 0으로 지정한 뒤 위 조건에 맞추어 재귀
    if (direction == 0 or direction == 'right') and num < A[m]:
        search(num, l, m - 1, 'left')
    elif (direction == 0 or direction == 'left') and num > A[m]:
        search(num, m + 1, r, 'right')

# 인풋!
for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())

    # A는 정렬한 상태로 리스트 A에 저장하기
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    # 정답 출력용 카운트
    cnt = 0

    # B를 순회하면서 B의 원소를 target 으로 이진 탐색을 실행함
    for i in B:
        search(i, 0, len(A)-1, 0)
    print(f'#{tc} {cnt}')
