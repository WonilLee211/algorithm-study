def enqueue(num):       #새 요소 삽입
    global N
    heap[N] = num
    temp = N
    flag = 1
    while temp>1:
        if heap[temp] > heap[temp//2]:
            heap[temp], heap[temp//2] = heap[temp//2], heap[temp]
            temp //= 2
        elif heap[temp] < heap[temp//2]:
            break
        else:
            print('error! 같은 값이 이미 존재합니다')
            flag = 0
            break
    if flag:
        N += 1


def dequeue():      #최대우선순위 삭제 후 반환
    global N
    result = heap[1]
    heap[1] = heap[N-1]
    heap[N-1] = 0
    temp = 1
    while temp < N-1:
        change = 0
        if N-1 > temp*2 and heap[temp*2] < heap[temp*2 +1]:
            change = 1
        if heap[temp]<heap[temp*2+change]:
            heap[temp], heap[temp*2+change] = heap[temp*2+change],heap[temp]
            temp = temp*2+change
        else:
            break
    N -= 1
    return result


def peak():         #최대 우선 순위 반환
    return heap[1]

heap = [0] * 16
N = 1
