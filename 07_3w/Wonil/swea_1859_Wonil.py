'''
조건
    1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
    2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
    3. 판매는 얼마든지 할 수 있다.
    4. 각 날의 매매가는 10,000이하이다.

예를 들어 3일 동안의 매매가가 1, 2, 3 이라면,
 처음 두 날에 원료를 구매하여 마지막 날에 팔면 3의 이익을 얻을 수 있다.

입력 :
첫 번째 줄 : 테스트 케이스의 수 T
각 테스트 케이스 별 첫 줄 : 자연수 N(2 ≤ N ≤ 1,000,000)
각 테스트 케이스 별 둘째 줄 : 각 날의 매매가를 나타내는 N개의 자연수들이 공백으로 구분

출력 :
각 테스트 케이스마다 ‘#{테스트케이스 번호} {최대 이익}'을 출력

알고리즘
1. 뒤에서 부터 비교
2. p[n-1] > p[n]라면
    earning 계산
    buylist 초기화
    maxprice = p[n-1] 변경

3. p[n-1] <= p[n]라면 max가격 유지
    - buylist.appned(p[n-1]에 추가

n = last idx부터 1까지

---
느낀점
연산력을 극대화 시키기 위해 최대한 함수 사용 피하고 메모리를 사용
'''
t = int(input())

for tc in range(1, t+1):
    n = int(input())

    prices = list(map(int,input().split()))

    max_price = prices[-1] # 뒤에서부터 비교하기 때문에 가장 큰 값을 prices 마지막 값으로 설정
    buy_list = buy_cnt = 0
    earning = 0

    for i in range(n-2, -1, -1): # 마지막의 앞 index부터 0까지

        if prices[i] <= max_price: # 현재의 max_price보다 작으면 사재기 가능_구매하기
            buy_list += prices[i]
            buy_cnt +=1

        else:   # 현재의 max_price보다 크면 사재기 못함_판매 & max_price 업데이트
            earning += max_price * buy_cnt - buy_list
            buy_list = buy_cnt = 0
            max_price = prices[i]

        if not i: # i = 0일 때 판매를 했거나 구매를 했거나 이기 때문에, 판매 과정 재실행
            earning += max_price * buy_cnt - buy_list
            break

    print(f"#{tc} {earning}")