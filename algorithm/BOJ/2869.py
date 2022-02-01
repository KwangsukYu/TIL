# h = v, am = a  pm = b  a b v

a, b, v = map(int, input().split())
goal = v - b
move = a - b

if goal % move:
    print(goal//move + 1)
else:
    print(goal//move)