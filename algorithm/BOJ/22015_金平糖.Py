A, B, C = map(int, input().split())
if A > B: B, A = A, B
if B > C: B, C = C, B
print(C - A + (C - B))
