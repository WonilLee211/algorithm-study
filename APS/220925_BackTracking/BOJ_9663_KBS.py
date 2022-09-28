def f(i, N):                                            #대충 순열만든후 대각선 체크하는 재귀함수
    global ans
    if i == N:
        ans += 1
        #print(ans)
        return
    else:
        for j in range(i, N):
            mat[i], mat[j] = mat[j], mat[i]
            for k in range(i):
                if abs(k-i) == abs(mat[k]- mat[i]):
                    break
            else:
                f(i+1,N)
            mat[i], mat[j] = mat[j], mat[i]

N = int(input())
ans = 0
mat = list(range(N))                                    #절반만 봐요
for i in range(N//2):
    mat[0], mat[i] = mat[i], mat[0]
    f(1,N)
    mat[0], mat[i] = mat[i], mat[0]
ans = ans *2
if N % 2 == 1:                                         #홀수인경우
    mat[0], mat[N//2] = mat[N//2], mat[0]
    f(1,N)
    mat[0], mat[N//2] = mat[N//2], mat[0]
    
print(ans)