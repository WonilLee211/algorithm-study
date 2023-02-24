'''
1. 장애물 3개 > 빈 복도의 조합으로 생성
2. 상, 하, 좌, 우 각 방향에 대해서 직진으로 탐색
3. 탐색 중 어떤 조건을 만났을 때 대처
3-1. 장애물을 만났을 때 : 해당 방향 탐색 중지 (break)
3-2. 학생을 만났을 때 : 전체 탐색 중지 (return False)
4. 탐색이 모두 끝났을 때 : return True
5. 장애물 초기화 (빈 복도로 되돌려놓기)

1 ~ 5 과정 반복
'''

from itertools import combinations as cb

def watch():
    for teacher in teacher_list:
        x, y = teacher
        dxy_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for dxy in dxy_list:
            nx, ny = x, y
            while True:
                nx += dxy[0]
                ny += dxy[1]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    break
                if graph[nx][ny] == 'S':
                    return False
                if graph[nx][ny] == 'O':
                    break
    return True


if __name__ == '__main__':
    N = int(input())
    graph = [input().split() for _ in range(N)]

    empty_list = []
    teacher_list = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'X':
                empty_list.append((i, j))
            elif graph[i][j] == 'T':
                teacher_list.append((i, j))

    # 장애물 3개 세우기
    for walls in cb(empty_list, 3):

        for wall in walls:
            x, y = wall
            graph[x][y] = 'O'
        if watch():
            print('YES')
            break
        # 장애물 초기화
        for wall in walls:
            x, y = wall
            graph[x][y] = 'X'
    else:
        print('NO')