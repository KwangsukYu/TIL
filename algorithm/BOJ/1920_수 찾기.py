N = int(input())
nums1 = list(map(int, input().split()))
M = int(input())
nums2 = list(map(int, input().split()))
def check(s, e, n):
    while s <= e:
        middle = (s + e) // 2

        if nums1[middle] == n:
            return 1
        elif nums1[middle] > n:
            e = middle - 1
        else:
            s = middle + 1
    return 0

s = 0
e = len(nums1) - 1
nums1.sort()

for i in nums2:
    print(check(s, e, i))