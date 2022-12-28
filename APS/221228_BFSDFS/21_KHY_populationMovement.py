import sys
input = sys.stdin.readline
# sys.stdin = open('BAEKJOON_16234.txt')
# T = int(input())

def BFS(x, y):
    q = [[x, y]] # 탐색할 queue
    union = [[x, y]] # 연합 좌표 리스트
    total_p = country[x][y] # 연합 국가 총 인구수
    while q:
        x, y = q.pop(0)
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(country[x][y] - country[nx][ny]) <= R:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    union.append([nx, ny])
                    total_p += country[nx][ny]
    return union, total_p

# for tc in range(1, T+1):

N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
cnt = 0 # 인구 이동이 일어나는 기간

while True:
    move = 0 # 연합이 일어난 횟수
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                union, total_p = BFS(i, j)
                # print(union, total_p, 1)
                if 1 < len(union):
                    move += 1
                    for x, y in union:
                        country[x][y] = total_p // len(union)

    if not move:
        break
    else:
        cnt += 1

print(cnt)



