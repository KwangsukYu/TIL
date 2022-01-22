T = int(input())

for i in range(T):
    testcase = int(input())
    score = list(map(int, input().split()))
    num_dict = {}
    for k in score:
        if num_dict.get(k) is None:
            num_dict[k] = 1
        else:
            num_dict[k] += 1      
    maxi = max(num_dict.values())   
    maxi_list = []
    for j in num_dict:
        if num_dict.get(j) == maxi:
            maxi_list.append(j)
    answer = max(maxi_list)
    
    print('#{0} {1}'.format(i+1, answer))