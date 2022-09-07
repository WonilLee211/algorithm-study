import sys
sys.setrecursionlimit(20010)


def bfs():
    if queue:
        starting = queue.pop(0)
        for i in grape[starting]:
            if arr[i] == 0:
                arr[i] = arr[starting] +1
                queue.append(i)
                print(queue)
        bfs()


N, M = map(int,input().split())
grape = [[] for _ in range(N+1)]
arr = [0] * (N+1)
queue = [1,]
for i in range(M):
    starting, ending = map(int, input().split())
    grape[starting].append(ending)
    grape[ending].append(starting)
arr[1] = 1
bfs()

x,y,z = arr.index(max(arr)), arr[arr.index(max(arr))]-1, arr.count(max(arr))
print(x,y,z)


"""
1.dfs는 시간초과
2.N*N grape는 메모리초과
3. 재귀 깊이 변경해주자
4. 내부함수 쓰니까 좋다
"""