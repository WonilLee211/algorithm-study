# 편집 거리

import sys
sys.stdin = open('input.txt')

def dist(word1,word2):
    n = len(word1)
    m = len(word2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = i #첫행 초기화
    for j in range(1, m + 1):
        dp[0][j] = j #첫열 초기화

    for i in range(1, n + 1):
        for j in range(1, m + 1):
     #문자가 같다면 왼쪽 위에 해당하는 수를 그대로 대입
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
     #문자가 다르다면, 3가지 경우 중에서 최솟값 찾기
            else: #삽입(왼쪽), 삭제(위쪽), 교체 (왼쪽 위) 중에서 최소 비용
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    return dp[n][m]
word1 = 'sunday'
word2 = 'saturday'

print(dist(word1,word2))