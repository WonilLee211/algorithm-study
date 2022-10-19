#1.

def solution(fees, records):
    answer = []
    data = [[0]*10000 for _ in range(2)]    #주차시작시간, 총 주차시간
    data[0] = [-1]* 10000       #주차 시작 시간 -1로 초기화
    for record in records:
        time = int(record[:2])*60 + int(record[3:5])
        car = int(record[6:11])
        in_out = record[11:13]
        if in_out == 'IN':                     #들어오면 주차시작시간 갱신
            data[0][car] = time
        elif in_out == 'OU':                    #나가면 주차시작시간=-1, 총주차시간 +=
            data[1][car] += time - data[0][car]
            data[0][car] = -1
    for i in range(10000):                         #아직 안나간 차가 있으면 주차시간 계산
        if data[0][i]!=-1:
            data[1][i] += 23*60 + 59 - data[0][i]
            
    for i in data[1]:
        if 0<i<= fees[0]:                           #기본요금
            answer.append(fees[1])
        elif i > fees[0]:                           #추가요금
            temp = (i-fees[0])/fees[2]
            if temp > int(temp):
                temp = int(temp)+1
            answer.append(fees[1]+temp*fees[3])
    return answer