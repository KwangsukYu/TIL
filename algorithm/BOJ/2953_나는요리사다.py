arr = [list(map(int, input().split())) for _ in range(5)]

number = 0
max_score = 0

for i in range(5):
    score = sum(arr[i])
    if score > max_score:
        max_score = score
        number = i + 1

print(number, max_score)