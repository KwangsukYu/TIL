import sys
sys.stdin = open('sample_input.txt')

# 인풋 받기
for tc in range(1, int(input())+1):
    M, N = map(int, input().split())
    cont = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    # 갈 수 있는 컨테이너 리스트
    nanganda = []

    # 트럭과 컨테이너리스트에 값이 존재하면 반복
    while cont and truck:

        # 두 리스트의 최대값을 골라서
        con = max(cont)
        tru = max(truck)

        # 트럭에 실을 수 있으면 난간다에 추가하고 원본 리스트에서 두개의 값을 삭제
        if con <= tru:
            nanganda.append(con)
            cont.remove(con)
            truck.remove(tru)
        # 트럭에 실을 수 없으면 컨테이너만 삭제
        else:
            cont.remove(con)

    # 난 간다가 비어있으면 컨테이너를 못 옮긴 것으로 0 출력, 아니면 난간다의 합 출력
    print(f'#{tc}', end=' ')
    print(0) if not nanganda else print(sum(nanganda))