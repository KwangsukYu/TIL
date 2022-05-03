# N = int(input())
# reco = int(input())
# order = list(map(int, input().split()))

# # name = 사진틀, cnt = 득표 수
# # 1.학생들이 추천을 시작하기 전에 모든 사진틀은 비어있다.
# name = []
# cnt = []

# #2. 어떤 학생이 특정 학생을 추천하면, 추천받은 학생의 사진이 반드시 사진틀에 게시되어야 한다.
# for i in range(reco):

#     # 4.현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가시킨다.
#     if order[i] in name:
#         cnt[name.index(order[i])] += 1

#     elif not name or len(name) < N:
#         name.append(order[i])
#         cnt.append(1)

#     # 3. 비어있는 사진틀이 없는 경우에는 현재까지 추천 받은 횟수가 가장 적은 학생의 사진을 삭제하고, 그 자리에 새롭게 추천받은 학생의 사진을 게시한다. 
#     # 이때, 현재까지 추천 받은 횟수가 가장 적은 학생이 두 명 이상일 경우에는 그러한 학생들 중 게시된 지 가장 오래된 사진을 삭제한다.
    
#     else:
#         # 최저 득표수와 그 인덱스를 담을 변수
#         min_reco = 1000000
#         min_i = 0

#         # 리스트에 추천 순서대로 들어가니까
#         # 최소값이 같을 경우 갱신을 안해주면 결국 가장 오래된 사진이 걸림
#         for idx in range(N):
#             if cnt[idx] < min_reco:
#                 min_reco = cnt[idx]
#                 min_i = idx

#         # 그 인덱스를 뽑아주고 새로운 사진을 집어 넣기
#         a = name.pop(min_i)
#         b = cnt.pop(min_i)
#         name.append(order[i])
#         cnt.append(1)

# # ans = list(zip(name, cnt))
# # ans.sort(key=lambda x:x[1], reverse=True)

# # 정렬 후 출력
# name.sort()
# for i in name:
#     print(i, end=' ')

# N = int(input())
# rec = int(input())
# numbers = list(map(int, input().split()))

# student = [0]*101
# board = []
# student[0] = 10000000
# for num in numbers:
#     if len(board) < N:
#         if num in board:
#             student[num] += 1
#         else:
#             board.append(num)
#             student[num] += 1
#     else:
#         if num in board:
#             student[num] += 1
#         else:
#             min_num = board[0]
#             min_v = 100000
#             for i in range(N):
#                 if min_v > student[board[i]]:
#                     min_num = board[i]
#                     min_v = student[board[i]]
#             board.pop(board.index(min_num))
#             student[min_num]=0
#             board.append(num)
#             student[num]+=1


# board.sort()
# print(*board)

