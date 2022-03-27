import math
import sys


# 인덱스 조절부분이 어려워서 클론코딩했다.
# 참고하면서 공부하기
def find_mod(n):

    count=0
    num=list()
    a=[0]*8001
    for i in range(len(n)):
        a[4000+n[i]]+=1


    b=a.index(max(a))
    c=max(a)
    a[b]=0

    if c!=max(a):
        return b-4000 

    else:
        return a.index(max(a))-4000 

T=int(sys.stdin.readline().rstrip())
T_list=list()
for i in range(T):
    T_list.append(int(sys.stdin.readline().rstrip()))

T_list_sort=T_list
T_list_sort.sort()

print(round(sum(T_list)/len(T_list)))
print(T_list_sort[math.trunc(len(T_list)/2)])
print(find_mod(T_list))
print(T_list_sort[len(T_list_sort)-1]-T_list_sort[0])