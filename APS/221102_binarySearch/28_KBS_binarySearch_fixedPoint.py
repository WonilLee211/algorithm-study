import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
strt = 0
nd = N-1
mid = (strt+nd)//2

while mid != arr[mid]:
    if mid > arr[mid]:
        strt = mid + 1
        mid = (strt + nd)//2
    elif mid < arr[mid]:
        nd = mid - 1
        mid = (strt + nd)//2
    if mid == strt or mid == nd or mid == arr[mid]:
        break

if mid == arr[mid]:
    print(mid)
else:
    print(-1)
