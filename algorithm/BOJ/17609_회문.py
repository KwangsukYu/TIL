# def is_palindrome(t):
#     global flag

#     def is_pseudo(t):
#         if t == t[::-1]:
#             return True
#         else:
#             return False
    
#     i = 0
#     j = len(t) - 1

#     while i < j:
#         if t[i] != t[j]:
#             if abs(i-j) > 1:
#                 case_1 = is_pseudo(t[i:j])
#                 case_2 = is_pseudo(t[i+1:j+1])

#                 if case_1 and flag:
#                     j -= 1
#                     flag = False
#                 elif case_2 and flag:
#                     i += 1
#                     flag = False
#                 else:
#                     print(2)
#                     return
#             else:
#                 print(2)
#                 return

#         i += 1
#         j -= 1
    
#     if flag:
#         print(0)
#         return
#     else:
#         print(1)
#         return


# # 인풋
# N = int(input())

# for i in range(N):
#     flag = True
#     text = input()
#     is_palindrome(text)


import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    word = input().rstrip()
    start = 0
    end = len(word)-1
    while True:
        if start >= end:
            print(0)
            break
        if word[start] == word[end]:
            start += 1
            end -= 1
        else:
            word1 = word[start+1:end+1]
            word2 = word[start:end]
            if word1 == word1[::-1] or word2 == word2[::-1]: # 둘중하나가 참이면 유사 회문
                print(1)
                break
            else:
                print(2)
                break

            # if word[start+1] == word[end]:        
            #     check = word[start+1:end+1]
            #     if check == check[::-1]:          # 여기 if문으로 들어왔을때 따로 else구문이없어서 시간초과?
            #         print(1)
            #         break
            # if word[start] == word[end-1]:
            #     check = word[start:end]
            #     if check == check[::-1]:          # 여기도 마찬가지?
            #         print(1)
            #         break
            # else:
            #     print(2)
            #     break

