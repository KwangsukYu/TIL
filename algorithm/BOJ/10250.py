T = int(input())

for testcase in range(T):
    H, W, N = map(int, input().split())
    floor_list = [j for j in range(1, H+1)]
    room_list = [i for i in range(1, W+1)]
    cnt = 0
    for r in range(1, len(room_list) + 1):
        for f in range(1, len(floor_list) + 1):    
            cnt += 1
            if cnt == N:
                if r < 10:
                    r = '0' + str(r) 
                else:
                    r = str(r)
                print(str(f) + r)



