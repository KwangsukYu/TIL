import sys
sys.stdin = open('sample_input.txt')

def check(e, idx, cnt):
    global max_cnt

    # 만약 인덱스가 최대 범위면 최대값 갱신 후 종료
    if idx == len(time_lst):
        if cnt > max_cnt:
            max_cnt = cnt
        return

    # 만약 시작시간이 전 종료시간 보다 크거나 같으면 종료시간을 다음 작업의 종료시간으로 바꾸고 함수 실행
    if time_lst[idx][0] >= e:
        check(time_lst[idx][1], idx+1, cnt + 1)

    # 이 작업을 건너 뛴 상황이 있을 수 있으므로 실행
    check(e, idx+1, cnt)



for tc in range(1, 1 + int(input())):
    N = int(input())
    time_lst = []
    max_cnt = 0

    # 반복문을 돌면서 s, e를 튜플 형식으로 time_lst에 넣어주고 가장 늦게 끝나는 시간을 갱신해줌
    for i in range(N):
        s, e = map(int, input().split())
        time_lst.append((s, e))

    # 튜플 형식으로 된 리스트를 정렬 하고, 같은 시간에 시작해서 늦게 끝나는 작업이 있는 경우 삭제할 del_lst 생성
    time_lst.sort()
    del_lst = []
    print(time_lst)
    # 정렬 되어 있으므로 순서대로 비교하면서 만약 시작 시간이 갖고 끝 시간이 다르면 del_lst에 추가
    for i in range(N-1):

        # 둘다 같으면 그냥 무시한다 == 나중에 set할 때 문제가 생김
        if time_lst[i] == time_lst[i+1]:
            pass
        elif time_lst[i][0] == time_lst[i+1][0]:
            del_lst.append(time_lst[i+1])

    # 두 리스트를 셋으로 변경후 정렬해주면 깔끔하게 나온다!
    time_lst = sorted(list(set(time_lst) - set(del_lst)))
    print(time_lst)

    # 그리고 각각 시간마다 돌면서
    for i in range(len(time_lst)-1):
        check(time_lst[i][1], i+1, 1)

    print(f'#{tc} {max_cnt}')