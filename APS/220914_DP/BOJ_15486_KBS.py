"""
import sys
N = int(input())
tp = [[0]*(N+1) for _ in range(3)]
for i in range(N):
    tp[0][i], tp[1][i] = map(int, sys.stdin.readline().split())
temp = 0
ans = 0
for i in range(N):
    if i + tp[0][i] <= N:
        tp[2][i+tp[0][i]] = max(tp[1][i]+tp[2][i], tp[1][i]+temp, tp[2][i+tp[0][i]])
        if temp < tp[2][i]:
            temp = tp[2][i]
        if ans < tp[2][i+tp[0][i]]:
            ans = tp[2][i+tp[0][i]]
print(ans)

???
"""

import sys
N = int(input())
tp = [[0]*(N+2) for _ in range(3)]
for i in range(1, N+1):
    tp[0][i], tp[1][i] = map(int, sys.stdin.readline().split())
ans = 0
for i in range(1, N+1):
    if tp[2][i] < tp[2][i-1]:
        tp[2][i] = tp[2][i-1]
    if i + tp[0][i] <= N+1 and tp[2][i+tp[0][i]] < (tp[1][i]+tp[2][i]):
        tp[2][i+tp[0][i]] = tp[1][i]+tp[2][i]
        if ans < tp[2][i+tp[0][i]]:
            ans = tp[2][i+tp[0][i]]
print(ans)