
def fibonacci6(n):
    if n < 2:
        return n
    elif n in fibo: #저장된 값이면 리턴
        return fibo[n]
    else:
        if n%2 == 0:    #짝수
            temp = ((fibonacci6(n//2)**2) +2*(fibonacci6(n//2)*fibonacci6(n//2-1)))%D
            fibo[n] = temp  #저장 안됬으면 저장
            return temp
        else:           #홀수
            temp =((fibonacci6(n//2)**2) + (fibonacci6(n//2+1)**2))%D
            fibo[n] = temp
            return temp

            
n = int(input())
fibo = {                #메모이제이션
    0: 0,
    1: 1,
}
D = 1000000007
print(fibonacci6(n))