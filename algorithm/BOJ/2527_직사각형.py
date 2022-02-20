def my_max(a, b):
    return a if a > b else b

def my_min(c, d):
    return c if c < d else d

for _ in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())
# 어느게 어디로 주어질지 모르니까
    dist_x = my_max(x1, x2) - my_min(p1, p2)
    dist_y = my_max(y1, y2) - my_min(q1, q2)
# 직사각형 여러개 그려보면서 찾아보면... 
    if dist_x < 0 and dist_y < 0:
        print('a')
    elif dist_x > 0 or dist_y > 0:
        print('d')
    elif dist_x == 0 and dist_y == 0:
        print('c')
    else:
        print('b')

    
    
