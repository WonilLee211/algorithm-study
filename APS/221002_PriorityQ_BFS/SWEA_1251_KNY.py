# 하나로
# 총 환경 부담금을 최소로 지불하며, N개의 모든 섬을 연결할 수 있는 교통 시스템을 설계

# 크러스컬 알고리즘

from itertools import combinations
import sys
sys.stdin = open('input.txt')

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b


T = int(input())

for tc in range(1,1+T):
    N = int(input())

    xs = list(map(int,input().split()))
    ys = list(map(int,input().split()))

    E = float(input())

    edges = []
    result = 0

    parent = [0] * (N+1)

    for i in range(1,N+1):
        parent[i] = i

    island = []
    for i in range(N):
        x,y = xs[i], ys[i]
        island.append((i,x,y))  # 노드번호, 노드x좌표, 노드y좌표

    island_comb = list(combinations(island,2))  # 연결될 수 있는 섬 조합 구하기

    for comb in island_comb:
        a, b = comb[0][0], comb[1][0]   # 노드 번호

        L = ((comb[0][1]-comb[1][1])**2+(comb[0][2]-comb[1][2])**2) # 환경부담금 => 환경 부담 세율(E)과 각 해저터널 길이(L)의 제곱의 곱(E * L^2)만큼 지불
        w = L * E
        edges.append((w,a,b))   # 환경부담금을 비용으로 하여 정렬 # 환경부담금, 노드1, 노드2

    edges.sort()

    for edge in edges:
        w, a, b = edge

        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            result += w
    print(f'#{tc} {round(result)}')