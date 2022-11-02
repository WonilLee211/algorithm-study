'''N = int(input())
flag = 0
inf = 10**8
ans = [0] * inf
ans[1] = 1
for i in range(inf):
    if ans[i]:
        flag+= 1
        if flag == N:
            print(i)
            break
        else:
            for j in (2,3,5):
                if i*j< inf:
                    ans[i*j] = 1'''

N = int(input())
cnt2,cnt3,cnt5 = 1,1,1
x,y,z = 2, 3, 5
ans = [0]* (N+1)
ans[1] = 1

for i in range(2,N+1):
    ans[i] = min(x,y,z)
    if ans[i] == x:
        cnt2 += 1
        x = ans[cnt2] *2
    if ans[i] == y:
        cnt3 += 1
        y = ans[cnt3] *3
    if ans[i] == z:                           #elif로 하면 숫자갱신이 안되요
        cnt5 += 1
        z = ans[cnt5] *5

print(ans[N])
