'''
조건
N*N 크기의 단어 퍼즐을 만들 때, K 길이의 단어가 
들어갈 수 있는 자리 수
1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)
2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)

입력 :
첫 번째 줄 : 테스트 케이스의 수 T
각 테스트 케이스 별 첫 줄 :  N K
각 테스트 케이스 별 둘째 줄 ~ N+1줄:
    흰색 부분은 1, 검은색 부분은 0

출력 :
‘#{테스트케이스 번호} {정답}'

알고리즘
함수1
    행마다 x축방향으로 글자수와 동일한 공간 세기
함수2
    매트릭스 대각 대칭변환
알고리즘
1. 함수1로 입력된 퍼즐에서 들어갈 수 있는 공간 세기
2. 함수2로 퍼즐 대각대칭 변환
3. 함수1로 대각대칭된 퍼즐에서 들어갈 수 있는 공간 세기
---
느낀점
변수 초기화 위치를 계속 틀린다.
'''
# reduce함수를 연습삼아 써봄
from functools import reduce
T = int(input())

# 행마다 x축방향으로 글자 수와 동일한 공간 세기 
def cnt_space(matrix, k):
    # ['10101', ...] 형태를 [['1', '1', '1'], ...] 형태로 바꾼다.
    temp_puzzle = list(list(row.split('0')) for row in matrix)
    
    needed_space = '1'*k
    cnt = 0

    for row in temp_puzzle:
        for space in row:
            if space == needed_space:
                cnt += 1

    return cnt

# 퍼즐을 대각 대칭시키기
def oppositeangle_symmetry(matrix, n):
    temp_matrix = list()
    
    # ['10011', ..] 형태로 만들어서 반환 
    for i in range(n):
        new_row = '' # 위치를 잘못 두고 오래걸렸다.

        for j in range(n):
            new_row += matrix[j][i]
        temp_matrix.append(new_row)

    return temp_matrix


for tc in range(1, T+1):

    N, K = map(int, input().split())

    result = 0

    # 입력의 숫자 사이 공백 처리 
    data = list(list(input().split()) for _ in range(N))
    # 행의 값들을 문자열로 바꾸고 리스트로 감싸기
    puzzle = list(reduce(lambda acc,num : acc + num, data[i]) for i in range(N))

    result += cnt_space(puzzle, K)
    symmetry_puzzle = oppositeangle_symmetry(puzzle, N)
    result += cnt_space(symmetry_puzzle, K)

    print(f"#{tc} {result}")