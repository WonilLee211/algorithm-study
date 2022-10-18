N = int(input())
lesson = [0] * N
for i in range(N):
    temp = list(map(int,input().split()))
    for j in temp[1:]:                      #비트연산으로 밀어서 수업시간 나타내기   234-> 0X1110
        lesson[i] = lesson[i]|1<<j
M = int(input())
people = [0] * M
for i in range(M):
    temp = list(map(int,input().split()))
    for j in temp[1:]:
        people[i] = people[i]|1<<j

ans = [0] * M
for i in range(M):
    for j in range(N):
        if lesson[j] == lesson[j]&people[i]: #공강시간 내에 수업시간이 있으면 and연산시 수업시간과 같아야됨
            ans[i]+= 1


for i in ans:
    print(i)
