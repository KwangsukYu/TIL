N = int(input())
col, mac = map(int, input().split())

col //= 2

print(N if col + mac > N else col + mac)