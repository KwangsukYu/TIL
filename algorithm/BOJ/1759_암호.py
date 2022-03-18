L, N = map(int, input().split())
text = input().split()
text.sort()
visited = [0] * N

def check(string):
    for i in 'aeiou':
        string = set(string) - set(i)
    if len(string) == L or len(string) <= 1:
        return False
    else:
        return True


def DFS(idx, t):

    if len(t) == L:
        if check(t): 
            print(t)
        return

    if idx < N:
        DFS(idx + 1, t + text[idx])
        DFS(idx + 1, t)

DFS(0, '')
