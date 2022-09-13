def cardpack(n):
    if n == N:
        return
    temp = P[n]
    for i in range(n):
        if P[i] + ans[n-i-1] > temp:
            temp = P[i] + ans[n-i-1]
            #print(n, i, n-1, P[i], ans[n-i])
    ans[n] = temp
    cardpack(n + 1)

N = int(input())
P = list(map(int,input().split()))
ans = [0] * (N)
ans[0] = P[0]
cardpack(1)
print(ans[-1])