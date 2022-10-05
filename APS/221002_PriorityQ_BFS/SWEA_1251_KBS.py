tc = int(input())

for test in range(tc):
    N = int(input())
    pos = [list(map(int,input().split())) for _ in range(2)]
    E = float(input())
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = E*((pos[0][i]-pos[0][j])**2 +(pos[1][i]-pos[1][j])**2)
    ans = 0
    used = {0}
    while len(used) != N:
        temp = 2*10**12
        next = [0,0]
        for i in list(used):
            for j in range(N):
                if j not in used and arr[i][j]< temp:
                    temp = arr[i][j]
                    next = [i,j]
        ans += arr[next[0]][next[1]]
        used.add(next[1])

    print(f'#{test+1} {round(ans)}')
                