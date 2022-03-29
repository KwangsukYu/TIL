import sys
sys.stdin = open('sample_input.txt')

# triplet인지 확인하는 함수, 현재 플레이어의 카드리스트를 인자로 받는다.
def is_triplet(lst):

    # 셋으로 중복을 제거한 뒤(동일 숫자 계산 방지 1, 2, 2, 3) sorted함수로 정렬, 카운팅용 변수 생성
    new_lst = sorted(set(lst))
    max_cnt = 0
    cnt = 0

    # 정렬 된 리스트만큼 순회를 하며서 i번과 i+1번 인덱스의 차가 -1이면 cnt 추가
    # cnt가 max_cnt보다 크면 갱신, -1이 아니면 cnt를 0으로 초기화
    for i in range(len(new_lst)-1):
        if new_lst[i] - new_lst[i+1] == -1:
            cnt += 1

            if cnt > max_cnt:
                max_cnt = cnt
        else:
            cnt = 0

    # max_cnt 가 2 이상일 경우 True리턴
    # max_cnt == 2로 하면 1 2 4 뒤에 3이 들어왔을때 max_cnt는 3이 되버림
    if max_cnt >= 2:
        return True
    else:
        return False

# 인풋 받기
for tc in range(1, int(input())+1):

    # winner의 초기값은 무승부로 해두고 num_lst에 인풋을 받는다.
    winner = 0
    num_lst = list(map(int,input().split()))
    p1 = []
    p2 = []

    # 12번을 순회하면서 p1, p2에게 각각 카드를 나눠주고 3장 이상이 되면
    # 나누어 줄 때마다 run과 triplet 의 여부를 확인해준다.
    for i in range(12):

        # 짝수면 p1, 홀수면 p2에 추가 해주기
        if i % 2:
            p2.append(num_lst[i])

            # p가 3장이상 가지고 있을때 conut 함수로 그 카드가 run인지 확인
            # is_triplet함수로 triplet인지 확인 한 후 둘 중하나라도 있으면
            # winner를 변경해주고 반복 종료
            if len(p2) >= 3:
                if p2.count(num_lst[i]) == 3 or is_triplet(p2):
                    winner = 2
                    break

            # 위와 동일
        else:
            p1.append(num_lst[i])
            if len(p1) >= 3:
                if p1.count(num_lst[i]) == 3 or is_triplet(p1):
                    winner = 1
                    break

    print(f'#{tc} {winner}')
