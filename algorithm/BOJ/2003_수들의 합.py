N, M = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(N):
    stack = [arr[i]]
    tmp = 0
    idx = i
    while stack:
        v = stack.pop()
        tmp += v
        
        if tmp > M:
            break
        elif tmp == M:
            cnt += 1
            break
        else:
            if idx < N-1:
                idx += 1
                stack.append(arr[idx])

print(cnt)