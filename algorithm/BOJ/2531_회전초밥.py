'''
원래 회전 초밥은 손님이 마음대로 초밥을  고르고, 먹은 초밥만큼 식대를 계산하지만, 벨트의 임의의 한 위치부터 k개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공한다. 
각 고객에게 초밥의 종류 하나가 쓰인 쿠폰을 발행하고, 1번 행사에 참가할 경우 이 쿠폰에 적혀진 종류의 초밥 하나를 추가로 무료로 제공한다. 만약 이 번호에 적혀진 초밥이 현재 벨트 위에 없을 경우, 요리사가 새로 만들어 손님에게 제공한다.  
'''

# N 접시
# d 초밥 가짓수
# k 연속 접시
# c 쿠폰


# 완탐
def check(lst):
    checked_lst = set(lst)
    return len(checked_lst) if c in checked_lst else len(checked_lst) + 1

N, d, k, c = map(int, input().split())
``
sushi = []

for i in range(N):
    su = int(input())
    sushi.append(su)

sushi += sushi[:k]

j = k
selected = sushi[:k]
max_v = check(selected)

while j < len(sushi):
    selected.pop(0)
    selected.append(sushi[j])
    max_v = max(max_v, check(selected))

    j += 1

print(max_v)
