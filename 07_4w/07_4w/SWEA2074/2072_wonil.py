t = int(input())
for tc in range(t):
    num = 0
    li = list(map(int, input().split()))
    
    for i in li:
        if i%2:
            num +=i

    print(f"#{tc} {num}")