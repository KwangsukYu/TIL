# from itertools import combinations
# import sys

# # K 가 5보다 작으면 0 
# N, K = map(int, sys.stdin.readline().rstrip().split())
# sett = {"a", "i", "n", "t", "c"}
# if K < 5:
#     for i in range(N):
#         n = input()
#     print(0);exit()
# if K >= 26:
#     for i in range(N):
#         n = input()
#     print(N);exit
# K -= 5
# str_list = []
# words = []

# # aintc 를 공백으로 제거
# for i in range(N):
#     word = set(list(sys.stdin.readline().rstrip()))
#     test = word.difference(sett)
#     text = []
#     for j in test:
#         t = ord(j)-ord("a")
#         text.append(t)
#         str_list.append(t)
#     words.append(text)

# # 남은 K만큼 문자열을 조합
# comb = combinations(str_list, K)
# ans = 0

# # 조합된 문자열로 가장 많은 단어를 찾음
# for c in comb:
#     c = set(c)
#     v = 0
#     for i in words:
#         for j in i:
#             if j not in c:
#                 break
#         else:
#             v += 1
#     if v > ans:
#         ans = v

# # 시간초과...
# print(ans)


def nCr(r, start, selected):
    global answer
    # 종료 파트
    if r <= 0:
        cnt = 0
        for word in filtered_words:
            selected = set(selected)
            for char in word:
                if ord(char)-ord('a') not in selected:
                    break
            else:
                cnt += 1
            answer = max(cnt, answer)
        return

    # 유도 파트
    for i in range(start, len(letter)):
        nCr(r-1, i, selected + [letter[i][0]])


def my_filter(N):
    alphabet = [0] * 26
    words = list(set(input()) for _ in range(N))
    filtered_words = list()

    for word in words:
        temp = list()

        for char in word:
            if char not in 'antic':
                alphabet[ord(char)-ord('a')] += 1
                temp.append(char)

        filtered_words.append(temp)
    letter = list(zip(list(range(26)), alphabet))
    return letter, filtered_words, words, alphabet


N, K = map(int, input().split())
answer = 0

if K < 5:
    for i in range(N):
        n = input()
    print(0)

elif K == 26:
    for i in range(N):
        n = input()
    print(N)

else:

    letter, filtered_words, words, alphabet = my_filter(N)
    letter = list(filter(lambda x:True if x[1] else False, letter))
    letter.sort(key=lambda x:-x[1])
    nCr(K-5, 0, [])
    print(answer)