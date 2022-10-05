# 암호만들기
# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
# 알파벳이 암호에서 증가하는 순서로 배열

import sys
from string import ascii_lowercase
sys.stdin = open('input.txt')

def f(i,k,r):   # 순열로 암호 생성 (암호 조건으로 백트래킹)
    global result

    if i == r:
        if not len(set(p)&vowel) < 1 and not len(set(p)&cons) < 2:  # 암호 구성 조건  (모음하나이상,자음두개이상)
            if sorted(p) == p:  # 암호 순서 조건 (오름차순)
                result.append(''.join(p))   # 조건맞으면 result에 암호 append

    else:
        for j in range(k):
            if i >= 1:
                # 암호 순서 조건 (다음에 올 알파벳이 오름차순 아니면 continue) 백트래킹
                if alphabet_list.index(a[j]) < alphabet_list.index(p[i-1]):
                    continue
            if used[j] == 0:
                used[j] = 1
                p[i] = a[j]
                f(i+1, k, r)
                used[j] = 0

L,C = map(int,input().split())

alphs = list(input().split())

alphabet_list = list(ascii_lowercase)

vowel = {'a','e','i','o','u'}   # 모음
cons = set(alphabet_list) - vowel   # 자음

N = C
R = L
used = [0] * N
p = [0] * R
a = alphs
result = []
f(0, N, R)
for x in sorted(result):    # 오름차순 출력
    print(x)