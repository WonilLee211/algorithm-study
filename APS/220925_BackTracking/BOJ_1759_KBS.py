from itertools import combinations

L, C = map(int,input().split())
buffer = list(input().split())
moum = {'a', 'e', 'i', 'o', 'u'}
buffer.sort()

for hubo in combinations(buffer, L):
    moums = 0
    logic = 0
    for s in hubo:
        if s in moum:                   #O(1)
            moums += 1
            if moums > L-2:             #자음이 최소 2개니까  L-2보다 모음이 많으면 cut
                logic = 1
                break
    if logic:
        continue
    if 1 <= moums:
        print(''.join(hubo))