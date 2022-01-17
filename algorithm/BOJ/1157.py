# word = input().upper()
# upper_ = list(word)

# A = {}
# for i in upper_ :
#     if i in A :
#         A[i] += 1
#     else :
#         A[i] = 1

# B = []
# for key, value in A.items() :
#     if value == max(A.values()) :
#         B += key

# if len(B) == 1 :
#     print(B[0])
# else :
#     print("?")

# 대문자로 input 받고 딕셔너리 A에 알파벳 : 값 저장 B라는 리스트에 최대 밸류 값을 가진 키를 넣고 len(B)해서 중복 검사 1개가 아니면 "?" 출력
# 근데 너무 길다? 짧게 해야하는데...

# 풀이 찾아봄!
# https://www.byfuls.com/programming/read?id=49
inputData = input().upper()         # 나랑 똑같음
searchKeys = list(set(inputData))   # 중복 없음
 
countArr = []     # 빈 리스트
for key in searchKeys:    # 중복 없앤 거에서
    countArr.append(inputData.count(key))  # 중복 없앤거에서 각 알파벳이 몇 번 들어갔는지

if countArr.count(max(countArr)) > 1: # max값이 몇개인지 만약 한개 보다 크다면 중복임으로 "?"
    print("?")
else:
    print(searchKeys[countArr.index(max(countArr))]) # 중복 없으면 한개 출력 ㄷㄷ
