# 최적 경로
# 회사에서 출발해서 이들을 모두 방문하고 집에 돌아가는 경로 중 총 이동거리가 가장 짧은 경로

import sys
sys.stdin = open('input.txt')

def f(i,k,dis):
    global min_dis

    if dis >= min_dis:  # 최소 거리 넘으면 return 백트래킹
        return

    if i == k:
        dis += abs(p[-1][0]-home[0])+abs(p[-1][1]-home[1])  # 마지막 지점에선 집으로 오는 거리를 dis에 더해줌
        if dis < min_dis:
            min_dis = dis

    else:
        for j in range(k):  # 경로를 순열로 생성
            if used[j] == 0:
                used[j] = 1
                p[i] = a[j]
                if i == 0:  # 시작점에선 회사에서 출발하는 거리를 dis에 더해줌
                    f(i + 1, k, dis+abs(company[0]-a[j][0])+abs(company[1]-a[j][1]))
                else:   # 시작점 이후엔 집을 거치며 거리 추가

                    f(i+1, k, dis+abs(p[i-1][0]-a[j][0])+abs(p[i-1][1]-a[j][1]))
                used[j] = 0     # a[j]를 다른 자리에서 쓸 수 있도록 해제


T = int(input())

for tc in range(1,1+T):
    N = int(input())    # 고객의 수

    info = list(map(int,input().split()))

    company, home = info[:2], info[2:4]

    client = []
    for i in range(0,len(info[4:]),2):
        client.append(info[4:][i:i+2])

    a = client
    used = [0] * N
    p = [0] * N

    min_dis = 987654321
    f(0, N, 0)
    print(f'#{tc} {min_dis}')