from collections import deque

def BFS(s):
    q = deque()
    q.append(s)

    while q:
        v = q.popleft()

        # 만약 찾았으면 바로 코드 종료
        if v == K:
            print(lst[v])
            exit()

        for i in (v*2, v-1, v+1):

            # 인덱스 범위 안이고 미방문이면,,,
            # BFS기 때문에 첫 방문이 가장 적은 시간
            if 0 <= i < 100001 and lst[i] == -1:

                # 만약 2배면 q의 가장 처음으로 넣는다. 가중치가 0이기 때문
                if i == v*2:
                    lst[i] = lst[v]
                    q.appendleft(i)

                else:
                    # 나머지 부분 처리
                    lst[i] = lst[v] + 1
                    q.append(i)

                
            

N, K = map(int, input().split())
lst = [-1] * 100001
lst[N] = 0
BFS(N)