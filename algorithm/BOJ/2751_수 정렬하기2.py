import sys

N = int(sys.stdin.readline().rstrip())
h = []
for i in range(N):
    n = int(sys.stdin.readline().rstrip())
    h.append(n)

h.sort()

for i in h:
    print(i)
