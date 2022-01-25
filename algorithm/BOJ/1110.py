# N = input()
# num = N
# cnt = 0

# while True:
#     if len(num) == 1:
#         num = '0' + num
#     x = str(int(num[0]) + int(num[1]))
#     num = num[-1] + x[-1]
#     cnt += 1
#     if num == N:
#         print(cnt)
#         break
# 문자열 시간초과 난다아아아아아아 > 찾아보니 나만 그런게 아니다아아아앙아아ㅏ아

N = int(input())
num = N
cnt = 0

while True:
    x = num//10
    y = num % 10
    z = (x + y) % 10
    num = (y*10) + z
    cnt += 1

    if num == N:
        print(cnt)
        break