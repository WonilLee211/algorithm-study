T=int(input())
for t in range(1,T+1):
    Days=int(input())
    Price= list(map(int,input().split( )))
    Max=max(Price) #최댓값
    Ind=(Price.index(Max)) #최댓값 위치
    
    if Ind==0: #최댓값 위치가 가장 앞이면
        Ben=0
    else:
        Ben=0
        while len(Price)>0: #Price 리스트가 없을 때까지 반복
            Max=max(Price)
            Ind=(Price.index(Max))
            for i in range(0,Ind+1):
                Ben=Ben+(Max-Price[0])
                Price.remove(Price[0])
            
    print(f'#{t}',Ben)



