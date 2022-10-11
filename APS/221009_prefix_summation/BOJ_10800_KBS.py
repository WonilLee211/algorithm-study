import sys

N = int(input())
arr = [[] for _ in range(2001)]
color = [0] * (N+1)             #이전의 같은 색 공들의 부분합
hap = [0] * 2002                #모든 공들의 부분합
ans = [0] * (N+1)

for i in range(1,N+1):
    c,s = map(int,input().split())
    arr[s].append([c,i])        #공의색과 몇번째 공인지 공크기 열에 저장

for i in range(1,2001):
    hap[i] += hap[i-1]          #이전 부분합 더하고 각 공을 더해준다
    for j,num in arr[i]:        
        hap[i+1] += i
        ans[num] = hap[i] - color[j]    #전체 부분합에서 이전 같은 색의 부분합을 뻬서 정답 구함
    for j,num in arr[i]:
        color[j] += i                   #정답구하고 각 색 부분합 갱신 -> 같이 하면 같은색 같은크기공있는 케이스 안됨
for i in range(1,N+1):
    print(ans[i])