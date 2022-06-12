def BFS():
    q = [S]

    while q:
        v = q.pop(0)
        
        if v == G:
            print(stair[G])
            return

        if 0 < v+U <= F:
            if stair[v+U] == -1:
                stair[v+U] = stair[v] + 1
                q.append(v+U)
            
        if 0 < v-D <= F:
            if stair[v-D] == -1:    
                stair[v-D] = stair[v] + 1
                q.append(v-D)

    print('use the stairs')
    return


F, S, G, U, D = map(int, input().split())
stair = [-1] * (F + 1)
stair[S] = 0
BFS()