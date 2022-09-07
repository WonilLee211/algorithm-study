T=int(input()) # 첫번째 줄 = Test 케이스

for t in range(1,T+1): #1~T번 반복
    A,B = input().split() #2번째 줄 나눠서 N과 K 얻기
    N= int(A) # 가로세로 칸 수 결정
    K= int(B) # 글자 수!
    NUM_V=[] # 가로로 들어갈 수 있는 곳 수
    HOKAN =[] #세로줄 리스트
    NUM_H=[] # 세로로 들어갈 수 있는 곳 수
    Hori=[] # 세로 줄 이 들어갈 리스트

    for i in range(1,N+1): # N번 반복 
        Kan_V = list(map(int,input().split())) #1줄씩 리스트로 입력받기
        Kan_V.append(0)  # 앞과 뒤에 0 추가
        Kan_V.insert(0,0)
        Count_Kan_V = Kan_V.count(1) # 칸 갯수 확인       
        Count_seq = [] #연속된 칸인지 확인하기 위한 리스트
        

        if Count_Kan_V >= K:
            for j in range(0,N+2):
                try: 
                    Find_1 = Kan_V.index(1,j,N+2)       
                    Count_seq.append(Find_1)
                except ValueError :    
                    Count_seq.append(0)
        else:
            for i in range(0,N+2):
                Count_seq.append(0) 
        
        P_op = []
        Vasq = []
        v = Count_seq.pop(0)
        Vasq.append(v)
        while(len(Count_seq)>0):	
            vv = Count_seq.pop(0)	
            if v+1 == vv:		
                Vasq.append(vv)		
                v = vv	
            else:		
                P_op.append(Vasq)		
                Vasq = []		
                Vasq.append(vv)		
                v = vv
        
        P_op.append(Vasq)
        for i in range(0,len(P_op)):
            Seq_Num = len(P_op[i])
            if Seq_Num == K:
                NUM_V.append(1)
            else:
                pass
        
        Hori.append(list(Kan_V))     

    for i in range(1,N+1):
        for j in range(0,N):
            Chg = Hori[j][i]
            HOKAN.append(Chg)
            
        HOKAN.append(0)
        HOKAN.insert(0,0)
        Count_Kan_H = HOKAN.count(1)
        Count_Hseq = []

        if Count_Kan_H >= K:
            for j in range(0,N+2):
                try:
                    Find_2 = HOKAN.index(1,j,N+2)
                    Count_Hseq.append(Find_2)
                except ValueError :
                    Count_Hseq.append(0)
        else:
            for i in range(0,N+2):
                Count_Hseq.append(0)

        P_opH = []
        VasqH = []
        vH = Count_Hseq.pop(0) # 코멘트
        VasqH.append(vH)

        while (len(Count_Hseq)>0):
            vvH = Count_Hseq.pop(0)
            if vH+1 == vvH:
                VasqH.append(vvH)
                vH=vvH
            else:
                P_opH.append(VasqH)
                VasqH = []
                VasqH.append(vvH)
                vH=vvH
        P_opH.append(VasqH)
        for i in range(0,len(P_opH)):
            Seq_NumH = len(P_opH[i])
            if Seq_NumH == K:
                NUM_H.append(1)
            else:
                pass

        HOKAN=[]

    print(f'#{t}',len(NUM_H)+len(NUM_V))
