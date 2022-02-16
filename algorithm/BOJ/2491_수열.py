N = int(input())
num_list = list(map(int, input().split()))

min_cnt = 0
max_cnt = 0 
x_cnt = 0                               # 증가시 카운트
y_cnt = 0                               # 감소시 카운트
for i in range(1, N):               
    if num_list[i-1] <= num_list[i]:    # 앞 뒤 비교해서 증가하면
        x_cnt += 1                      # 증가 카운트 세주고
        if max_cnt < x_cnt:             # 최대값이랑 비교해서 계산해준다.
           max_cnt = x_cnt 
    else:
        x_cnt = 0
    
    if num_list[i-1] >= num_list[i]:    # 감소시도 마찬가지
        y_cnt += 1
        if max_cnt < y_cnt:
           max_cnt = y_cnt 
    else:
        y_cnt = 0



print(max_cnt + 1)                      # 최대값에 1을 더해야 총 길이가 됨