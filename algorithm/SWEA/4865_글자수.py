import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    cnt_dic = {}                        # 결과를 담을 딕셔너리
    str1 = input()
    str2 = input()

    for i in str1:
        cnt_dic[i] = cnt_dic.get(i, 0)  # 중복값이 있어도 키값이 전부 0
    # print(cnt_dic)

    for j in str2:                      # 해당하는 글자가 딕셔너리 키에 있으면 +1 아니면 pass
        try:
            cnt_dic[j] += 1
        except KeyError:
            pass
    # print(cnt_dic)

    ans = 0
    for v in cnt_dic.values():          # 밸류값을 순회돌면서 최대값을 찾고 출력해줌
        if v > ans:
            ans = v
    print(f'#{tc} {ans}')
