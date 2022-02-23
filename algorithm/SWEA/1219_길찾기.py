import sys
sys.stdin = open('input.txt')

def dfs(start, end):            # 인접리스트로 풀어보려고 리스트 형식으로 풀이하였다.
    stack = []
    for i in adjlist[start]:    # 빈 스택과 출발 정점에서 갈 수 있는 정점을 stack에 추가해줬다.
        stack.append(i)

    while stack:                # stack이 빌때 까지 pop으로 꺼내고
        v = stack.pop()
        if v == end:            # 만약 pop으로 꺼낸게 end랑 같으면 1을 리턴
            return 1

        if adjlist[v]:              # 아니면 v라는 정점에서의 경로가 있는지 없는지 확인
            for i in adjlist[v]:    # 있으면 stack에 다시 추가하고 반복하는 형식
                stack.append(i)     # 만약에 없으면 처음으로 돌아가서 그 다음 pop을 진행한다!
    return 0

for T in range(10):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))
    adjlist = [[] for _ in range(100)]      # 인풋을 인접리스트로 받음

    for i in range(E):
        n1, n2 = arr[i*2], arr[i*2+1]      # 이부분은 아직이해가 안되지만 받는 형식은 정해져있다고함
        adjlist[n1].append(n2)             # 일방향이기에 이런식으로 만들어 줌

    start = 0                              # 시작점
    end = 99                               # 도착점

    print(f'#{tc} {dfs(start, end)}')      # 형식에 맞게 출력





