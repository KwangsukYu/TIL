# 정수 n이면 n과 n의 각 자리수 더하기 d(75) = 75 + 7 + 5
num_list = []
for i in range(127, 130):
    c = i//10000
    a = i//1000
    b = i//100
    x = i//10
    y = i % 10
    i = i + x + y + a + b + c
    num_list.append(i)

print(num_list)
# for j in range(1, 150):
#     if j not in num_list:
#         print(j)

127 + 1 + 27 + 7 