import sys
T = int(sys.stdin.readline().strip())
lst = []

for i in range(T):
    word = sys.stdin.readline().strip()
    lst.append((len(word), word))

set_lst = list(set(lst))
set_lst.sort()

for x, y in set_lst:
    print(y)