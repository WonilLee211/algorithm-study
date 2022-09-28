def dfs(i,expect):                                                                      # brunch and bound 기법
    global ans                                                                          # 각 출발점에서 갈수있는 최소값들의 합을 기대값(아직안간 노드에서)
    if expect > ans:                                                                    # 현재 온 거리 + 기대값 < ans 이면 return 
        return
    if i == N+1:
        expect = expect-short[arr[i-1]] + graph[arr[i-1]][1]
        if expect < ans:
            ans = expect
        return
    else:
        for j in range(i,N+1):
            arr[i], arr[j] = arr[j], arr[i]
            dfs(i+1,expect-short[arr[i-1]]+graph[arr[i-1]][arr[i]])
            arr[i], arr[j] = arr[j], arr[i]
tc = int(input())
for test in range(tc):
    N = int(input())
    ans = 200 * 12
    point = list(map(int,input().split()))
    arr = list(range(N+2))
    arr.pop(1)                                      


    graph = [[0]*(N+2) for _ in range(N+2)]
    for i in range(N+2):
        for j in range(N+2):
            if i == j:
                graph[i][j] = 110                                                         # 0이면 min을 못써서
            else:
                graph[i][j] = abs(point[2*i]- point[2*j])+abs(point[2*i+1]- point[2*j+1]) #거리 저장 

    short = [0] * (N+2)
    for i in range(N+2):
        short[i] = min(graph[i])
    dfs(1,sum(short)-short[1])
    print(f'#{test+1} {ans}')
