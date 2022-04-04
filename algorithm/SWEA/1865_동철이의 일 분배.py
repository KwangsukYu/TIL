import sys
sys.stdin = open('input.txt')

# 행의 시작점과 방문 체크용 배열, 합을 인자로 받아서 함수 실행
def f(r, visited, ssum):
    global ans

    # 만약 마지막 줄까지 도달했으면 정답 갱신
    if r == N:
        if ssum > ans:
            ans = ssum
        return

    # 결국 소수를 곱하는 것이기 때문에 곱할 수록 작아진다.
    # 그래서 현재 합이 정답보다 작으면 바로 리턴
    if ssum <= ans:
        return

    # 현재 행이 r이고 열은 i가 되므로 i를 순회하면서 방문하지 않았으면
    # 방문 체크후 ssum에 소수점자리를 곱해주면서 재귀, 돌아올 때 배열 초기화
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            f(r+1, visited, ssum*arr[r][i]*(10**-2))
            visited[i] = 0

# 인풋값을 받는 곳
for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 방문 체크용 visited 배열
    visited = [0] * N

    # 글로벌 변수
    ans = 0

    # 함수 실행 행을 기준으로 내려가면서, visted, ssum을 원소로 받음(1로 한 건 곱하면 같기 때문)
    f(0, visited, 1)

    #처음에 라운드함수를 썼었는데 포맷팅으로도 가능하다.
    print(f'#{tc} {ans*100:6f}')

