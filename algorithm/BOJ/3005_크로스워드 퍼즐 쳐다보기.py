R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
words = []
for i in range(R):
    word = ''
    for j in range(C):
        if arr[i][j] == '#':
            words.append(word)
            word = ''
        else:
            word = word + arr[i][j]
    words.append(word)


for j in range(C):
    word = ''
    for i in range(R):
        if arr[i][j] == '#':
            words.append(word)
            word = ''
        else:
            word = word + arr[i][j]
    words.append(word)


words.sort()
for i in words:
    if len(i) >= 2:
        print(i)
        break