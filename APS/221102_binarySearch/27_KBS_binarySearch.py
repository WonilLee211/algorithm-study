#정렬된 배열에서 특정수의개수 구하기
N, x = map(int, input().split())
arr = list(map(int, input().split()))
arr.append(10**10)
arr.insert(0,-1*10**10)
sttato = 0
endo = N + 1
mid = (sttato + endo)//2
print(arr)

while not (arr[mid] == x and arr[mid-1] != x):
    if arr[mid] > x:
        endo = mid-1
    elif arr[mid] < x:
        sttato = mid+1
    else:
        if arr[mid-1] != x:
            break
        else:
            endo = mid-1
    mid = (sttato + endo)//2
    if endo == mid:
        break

print(sttato, mid, endo)
temp = mid
sttato = 0
endo = N + 1
mid = (sttato + endo)//2

while not (arr[mid] == x and arr[mid+1] != x):
    if arr[mid] > x:
        endo = mid-1
    elif arr[mid] < x:
        sttato = mid+1
    else:
        if arr[mid+1] != x:
            break
        else:
            sttato = mid+1
    mid = (sttato + endo)//2
    if endo == mid:
        break

print(sttato, mid, endo)
if arr[mid]== x:
    print(mid-temp+1)
else:
    print(-1)