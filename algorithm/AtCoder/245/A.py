A, B, C, D = map(int, input().split())

Takahasi = (A, B, 'Takahashi')
Aoki = (C, D, 'Aoki')

lst = [Takahasi, Aoki]
lst.sort()

print('Takahashi') if A == C and B == D else print(lst[0][2]) 