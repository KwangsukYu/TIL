# a = input()
# b = input()
# c = input()
# d = input()
# e = input()
# f = input()
# g = input()
# h = input()
# i = input()

# nlist = [a, b, c, d, e, f, g, h, i,]
# mlist = list(map(int,nlist))
# maxn = max(mlist)

# print(maxn)
# print(mlist.index(maxn)+1)

nlist = []

for i in range (1, 10) :
    nlist.append(int(input()))

print(max(nlist))
print(nlist.index(max(nlist)) + 1)

# 첫 제출은 위에 걸로... 다음 부턴 반복문으로 편하게 합시다...