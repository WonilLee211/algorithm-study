def wall_dfs(wall_num):
    global max_area, cnt
    if wall_num == 3:
        queue = q[:]
        bfs(queue)
        cnt += 1
        temp = 0

        for j in range(1, N+1):
            temp += mat[j].count(0)
        if temp > max_area:
            max_area = temp
        for k in range(N+2):
            mat[k] = matrix[k][:]
        for k in range(1,3):
            num = walls[k]
            mat[num//M+1][num%M+1] = 1
        return
    else:
        for i in range(walls[-1]+1, N*M):
            if mat[i//M+1][i%M+1] == 0:
                x = i // M + 1
                y = i % M +1
                for n in range(8):                          #대각선까지
                    if mat[x+dx[n]][y+dy[n]] == 1:
                        mat[i//M+1][i%M+1] = 1
                        break
                else:
                    continue                                #근처에 1 블럭이 없으면 패스
                walls.append(i)
                wall_dfs(wall_num+1)
                walls.pop()
                mat[i//M+1][i%M+1] = 0 

                      
def bfs(queue):
    if queue:
        x,y = queue.pop(0)
        for n in range(4):                          #상하좌우
            if mat[x+dx[n]][y+dy[n]] == 0:
                x2, y2 = x+dx[n], y+dy[n]
                queue.append((x2, y2))
                mat[x2][y2] = 2
        bfs(queue)


dx = [-1, 1, 0, 0, -1, -1, 1, 1]                    #상하좌우 대각선
dy = [0, 0, 1, -1, -1, 1, -1, 1]

N, M = map(int,input().split())                     #입력
matrix = [list(map(int,input().split())) for _ in range(N)]
mat = [[] for _ in range(N+2)]

for i in range(N):
    matrix[i].append(1)
    matrix[i].insert(0,1)
matrix.insert(0, [1]*(M+2))                         # 1~N+1
matrix.append([1]*(M+2))                            # 1~M+1

cnt = 0
max_area = 0
q = []
walls =[-1]

for i in range(N+2):
    for j in range(1,M+1):
        if matrix[i][j] == 2:
            q.append((i,j))                         #바로 꺼낼수 있게
    mat[i] = matrix[i][:]
wall_dfs(0)
print(max_area)
#print(cnt)




