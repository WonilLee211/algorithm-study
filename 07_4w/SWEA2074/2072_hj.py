T=int(input()) 
# 테스트 케이스 입력

for t in range(1,T+1):
    Numbers= list(map(int,input().split( ))) #숫자 받기
    Ans=0 #답이 더해지는 매개변수
    for i in Numbers:
        if i%2!=0: # 2로 나누어지지 않으면 홀수
            Ans=Ans+i # 값 더하기
        else:
            pass
    print(f'#{t}',Ans) 
