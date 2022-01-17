H, M = map(int, input().split())

if H > 0 :
    if M < 45 :
        print(H-1, M+15)
    elif M == 45 :
        print(H, 0)
    else :
        print(H, M-45)
elif H == 0 :
    if M < 45 :
        print(23, M+15)
    elif M == 45 :
        print(H, 0)
    else :
        print(H, M-45)
# a,b=map(int,input().split());x=a*60+b-45;print(x//60%24,x%60)
#16줄 > 1줄 , 시간말고 분으로 계산해서 하는 듯?
