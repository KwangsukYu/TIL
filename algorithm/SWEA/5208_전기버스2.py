import sys
sys.stdin = open('sample_input.txt')

# 출발지 idx, 충전량, cnt를 인자로 받아서 함수 실행
def check(idx, energy, cnt):

    # 글로벌 변수 ans 설정
    global ans

    # 만약 현재 cnt가 ans보다 높으면 가지치기
    if cnt >= ans:
        return

    # 만약 마지막 정류장에 도착했으면 최소값 갱신
    if idx == station - 1:
        if cnt < ans:
            ans = cnt
        return

    # 만약 전 정류장에서 남은 에너지가 1인데 충전을 안하고 함수 호출해서 0이 되어버렸으면...
    # 도착지에 도착해서 0인 경우엔 위의 가지치기로 걸러져서 무시해도 된다!
    if energy == 0:
        return

    # 다음 정류장에서 충전지를 교체한 경우와 안 한경우로 나눠서 재귀호출
    # 처음에 0을 추가해준 이유도 다음 정류장을 기준으로 함수를 실행하기 때문
    check(idx+1, charger[idx+1], cnt + 1)
    check(idx+1, energy-1, cnt)


# 첫 인풋 값은 정류장 갯수, 뒤로 들어오는 값(N-1)은 각 정류장의 충전지량
# 첫 정류장부터 시작해서 진행하기 위해 도착지에 0추가
for tc in range(1, 1+int(input())):
    station, *charger = map(int, input().split()); charger.append(0)

    # 출력용 글로벌 변수
    ans = 100

    # 출발지, 출발 시 충전량, cnt 순
    check(0, charger[0], 0)
    print(f'#{tc} {ans}')