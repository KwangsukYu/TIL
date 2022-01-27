# 정수 n이면 n과 n의 각 자리수 더하기 d(75) = 75 + 7 + 5
num_list = []

def lenth_num(num):
    self_n = num
    for i in str(num):
        self_n += int(i)
    return self_n

for i in range(1, 10000):
    num_list.append(lenth_num(i))

for j in range(1, 10000):
    if j not in num_list:
        print(j)
