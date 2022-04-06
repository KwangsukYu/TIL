import sys
sys.stdin = open('sample_input.txt')

# union-find
def find(x):
    while x != lst[x]:
        x = lst[x]
    return x

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    # 대표 원소 배열
    lst = [i for i in range(N+1)]
    pair = list(map(int, input().split()))

    print('대표 원소 배열 :', lst)

    for i in range(0, M*2, 2):
        # 작은 값을 기준으로 갱신하기 위함
        if pair[i] > pair[i+1]: pair[i], pair[i+1] = pair[i+1], pair[i]

        # union
        lst[find(pair[i+1])] = find(pair[i])

        print(f'union : {pair[i]} and {pair[i+1]}', lst)

    for i in range(N+1):
        lst[i] = find(i)

    print('result :', lst)

    print(f'#{tc} {len(set(lst))-1}')

