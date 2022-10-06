# 문제집
# 1. N개의 문제는 모두 풀어야 한다.
# 2. 먼저 푸는 것이 좋은 문제가 있는 문제는, 먼저 푸는 것이 좋은 문제를 반드시 먼저 풀어야 한다.
# 3. 가능하면 쉬운 문제부터 풀어야 한다.

# 위상정렬 & 우선순위큐 (최소힙)
# 위상정렬 : 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열
# 우선순위큐 (최소힙) : 값이 낮은 데이터가 먼저 삭제

import heapq
import sys
sys.stdin = open('input.txt')

def topology_sort():
    global result

    q = []

    for i in range(1, N+1):
        if indegree[i] == 0:
            heapq.heappush(q, i)

    while q:
        now = heapq.heappop(q)

        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q,i)


N,M = map(int,input().split())

indegree = [0]*(N+1)

graph = [[] for i in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1


result = []
topology_sort()
print(*result)