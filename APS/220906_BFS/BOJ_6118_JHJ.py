import sys
sys.stdin=open('example.text')

def BFS(Graph, start, N):
    visited=[0]*(N+1)
    Q = []
    visited[start] = 1
    Q.append(start)
    while Q:
        t = Q.pop(0)

        for i in Graph[t]:
            if not visited[i]:
                Q.append(i)
                visited[i] = visited[t]+1

    return visited

N, M = map(int,input().split())

Graph = [[] for _ in range(N+1)]

for i in range(M):
    A,B=map(int, input().split())
    Graph[A].append(B)
    Graph[B].append(A)

TEM = BFS(Graph,1,N)
ANS = []
Max_tem = max(TEM)
ANS.append(TEM.index(Max_tem))
ANS.append(Max_tem-1)
ANS.append(TEM.count(Max_tem))

for i in ANS:
    print(i, end=' ')
print()