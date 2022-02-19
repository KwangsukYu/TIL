# T = int(input())
# len_lst = []
# for i in range(6):
#     d, cm = map(int, input().split())
#     len_lst.append(cm)

# while True:
# # 6각형 그려보면서 0~5까지 순서를 넣고 생각해보면  두개다 정답임, 기준점만 잘 잡으면 끝!
#     # if len_lst[0] > len_lst[2] and len_lst[1] > len_lst[5]:
#     if len_lst[1] > len_lst[3] and len_lst[2] > len_lst[0]:
#         break
#     for i in range(5):
#         len_lst[i], len_lst[i+1] = len_lst[i+1], len_lst[i]

# # print((len_lst[0]*len_lst[5] + len_lst[2] * len_lst[3]) * T)
# print((len_lst[3]*len_lst[4] + len_lst[0] * len_lst[1]) * T)

arr = [[1,2,3,],[4,5,6,],[7,8,9]]
c_arr = list(zip(*arr))
print(c_arr)