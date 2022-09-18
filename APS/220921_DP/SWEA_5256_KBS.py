arr = [[0] * 140 for _ in range(140)]
arr[0][0] = 1
arr[0][1] = 1
for i in range(139):
    for j in range(139):
        if arr[i][j] ==0:
            break
        else:
            arr[i+1][j] += arr[i][j]
            arr[i+1][j+1] += arr[i][j]

tc = int(input())

for test in range(tc):
    n,a,b = map(int,input().split())
    print(f'#{test+1} {arr[n-1][min(a,b)]}')
"""

11000
12100     2 = 1 + 1
13310     3 = 2 + 1
14641     4 = 3 + 1
          6 = 3 + 3
arr[i][j] = arr[i-1][j] +arr[i-1][j-1]

1 <= a,b <= 70
최대 배열의 크기는 141
좌우대칭이므로 사실 절반만 있어도됨! ->min(a,b)


"""