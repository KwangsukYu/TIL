N, num = map(int, input().split())
card_list = list(map(int, input().split()))
ans = 0
# 5 6 7 8 9
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if card_list[i] + card_list[j] + card_list[k] <= num:
                if card_list[i] + card_list[j] + card_list[k] > ans:
                    ans = card_list[i] + card_list[j] + card_list[k]

print(ans)