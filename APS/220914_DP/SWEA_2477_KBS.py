tc = int(input())
for test in range(tc):
    N, M, K, A, B = map(int, input().split())
    reception = [[], []]
    repair = [[], []]
    reception[0] = list(map(int, input().split()))
    repair[0] = list(map(int, input().split()))
    customer = list(map(int, input().split()))       #남은 고객 스택
    for i in range(0, K):                            #고객번호
        customer[i] = [customer[i], i+1]
    wait1 = []                                      #접수 대기 스택
    wait2 = []                                      #수리 대기 스택
    reception[1] = [0] * N                       #접수중
    repair[1] = [0] * M                          #수리중
    result = []                                     #결과 비교용
    t = 0
    while len(result) != K:
        while customer and t == customer[0][0]:
            wait1.append(customer.pop(0))           #[도착시간, 고객번호]
        for i in range(N):
            if reception[1][i] != 0:
                reception[1][i][3] += 1
                if reception[0][i] == reception[1][i][3]:
                    wait2.append(reception[1][i])
                    reception[1][i] = 0
            if wait1 and reception[1][i] == 0:
                reception[1][i] = [wait1[0][0], wait1[0][1], i+1, 0]  #[도착시간, 고객번호, 접수창고번호, 접수중인시간]
                wait1.pop(0)
        
        for i in range(M):
            if repair[1][i] != 0:
                repair[1][i][4] += 1
                if repair[0][i] == repair[1][i][4]:
                    result.append(repair[1][i])
                    repair[1][i] = 0
            if wait2 and repair[1][i] == 0:
                repair[1][i] = [wait2[0][0], wait2[0][1], wait2[0][2], i+1, 0]  #[도착시간, 고객번호, 접수창고번호, 수리창고번호, 수리중인시간]
                wait2.pop(0)
        t += 1
    ans = 0
    for i in range(K):
        if result[i][2] == A and result[i][3] == B:
           ans += result[i][1]
    if ans == 0:
        print(f'#{test+1} -1')
    else:
        print(f'#{test + 1} {ans}')

