# Algorithm Group Study

## INDEX

---

<details>
<summary> <h2> 참여 인원 <h2> </summary>
<div markdown="1">

 이원일, 조홍준, 강보성, 김나연

</div>
</details>

---

<details>
<summary> <h2> 스터디 방식 <h2> </summary>
<div markdown="1">
  - 횟수 : 약 주 1회(수요일)

- 알고리즘 이론 학습 후 코딩 연습
- 관련 문제 과제 및 코드 리뷰
- 스터디 전날 코드별로 질문 남기기
- 필수사항 !
  - 주석
  - 폴더 형식
      /071W/
    
          SWEA문제번호/
              README.md
              문제번호_영문이름.py

</div>
</details>

---

<details>
<summary> <h2> 스터디 <h2> </summary>
<div markdown="1">

  2022.07.22 <1주차 스터디>  
    - SWEA 1979 '어디에 단어가 들어갈 수 있을까'
     - 알고리즘 핵심 개념 : 
       1. 연속된 수 뽑아내기
       2. 대각 대칭 사용해서 행과 열을 바꾸기

    - SWEA 1859 '백만장자 프로젝트'
     1. 최대 이득이라는 개념에 따른 접근 방법
     2. 방대한 Input 값에 따른 메모리 사용 최소화
     3. 함수 사용이 늘면 연산 수가 늘어남에 따라 계산시간이 늘어난다.

  2022.08.16 <3주차 스터디>  

   - KMP알고리즘 복습
    - 알고리즘 핵심 개념 : 
      1. 패턴이 접두 문자부터 중복이 있을 때 lps 테이블을 만들어 
      2. 대각 대칭 사용해서 행과 열을 바꾸기
  
  2022.08.28 <4주차 스터디>  

   - IM시험 준비(기출문제 풀이)
    - 이차원 배열, 인덱싱 관련 문제 
  
  2022.08.31 <5주차 스터디>  
   - BFS 이론 발표
   - DFS 문제리뷰
    - SWEA 1716 - 완전탐색을 통한 최소 연결 거리 계산

  2022.09.08 <6주차 스터디>  
   - 재귀함수 이론 발표
   - BFS 문제리뷰
    - BOJ 14502 - BFS와 백트랙킹, 조합 활용한 솔루션 찾기/묘수: 1 주변에 놓도록 조건을 걸면 케이스가 줄어든다 !
    - BOJ 6118 - BFS의 정석 문제 / 데이터를 리스트와 딕셔너리 형태로 저장하는 차이
  
  2022.08.31 <7주차 스터디>  
   - BFS 이론 발표
   - DFS 문제리뷰
    - SWEA 1716 - 완전탐색을 통한 최소 연결 거리 계산

  2022.09.15 <8주차 스터디>  
   - 문제리뷰
     - BOJ 15486 _ DP _ 작은 단계에서부터 최대값을 구해서 현재의 최댓값을 구하는데 사용/ 미래의 dp값을 미리 저장하고 비교하면서 업데이트
     - BOJ 11052 _ DP _ 상동
     - SWEA 2477 _ 구현 : 문제의 제약조건 및 업무 알고리즘에 따라 구현
  
  2022.09.21 <9주차 스터디>
  - DP 문제 리뷰
    - BOJ_2502
    - BOJ_2193
    - SWEA 5256
  - 백트래킹 발표

  2022.09.28 <10주차 스터디>
  -  문제 리뷰
     - BOJ_1759 : dfs + backtracking 문제. 추가 조건에 따른 출력 제한.
     - BOJ_9663 : N-Queen 문제. 대각 처리 조건 abs(arr[i] - arr[j]) == abs(i - j)
     - SWEA_1247 : 최적 경로 문제. 고객 방문순서를 다 구하고 처리하는 방법. 방문순서를 구하는 과정과 구했을 때마다 처리하는 방법
  - 우선순위 큐 발표

  2022.10.05 <11주차 스터디>
  -  문제 리뷰
     - BOJ_1766 : 위상 정렬과 우선순위 큐를 이용하여 출력순서를 맞추는 문제
     - BOJ_9663 : 3차원 BFS 문제. 벽을 뚤을 수 있는 횟수를 3차원으로 표현
     - SWEA_1247 : MST 문제.  Kruskal or Dijkstra로 풀 수 있음
  - 누적 합, 구간합 발표

  2022.10.12 <12주차 스터디>
  -  문제 리뷰
     - BOJ_10800 : 색깔 공. 누적합을 이용하여 같은 색, 같은 크기 공 피한 값 계산
     - BOJ_11444 : 큰 수의 피보나치 계산. 행렬 곱/ 짝수 홀수 계산법
     - BOJ_11660 : 전형적인 누적합 구간합 문제
  - 비트 마스크 문제

  2022.10.19 <13주차 스터디>
  -  문제 리뷰
     - BOJ_2098 : 외판원 순회 문제_비트 필드를 이용한 DP
     - BOJ_14569 : 시간표 짜기_비트 자리수 비교 및 set을 이용한 비교
     - BOJ_16236 : BFS 우선순위 큐 및 정렬을 이용한 탐색
     - BOJ_17281 : 비트마스크를 이용한 순열만들기_야구 게임 구현
     - 2022_programmers_주차요금계산 : 조건에 따른 구현
  
  2022.10.26 <14주차 스터디>
  - [이것이 취업을 위한 코딩테스트다] part 3 DP 문제 리뷰
     - 31 : DP 각 위치에서 올 수 있는 모든 가능성의 경우를 비교 후 갱신
     - 32 : 상동
     - 33 : DP 미래의 dp값을 현재의 수익과 얻을 수 있는 기대 수익을 더한 값과 비교
     - 34 : DP를 이용한 LDS LIS 구현
     - 35 : 2, 3, 5을 곱한 값 중 최소값을 동적으로 배치하는 방법
     - 36 : A문자를 B문자로 바꾸기 위해서 삽입 교체 삭제 연산을 최소로 하는 프로그래밍
  
  2022.11.02 <15주차 스터디>
  - [이것이 취업을 위한 코딩테스트다] part 3 이진탐색 문제 리뷰
     - 27 : 이진 탐색(bisect모듈 활용 및 이진탐색 알고리즘)
     - 28 : 이진 탐색(bisect모듈 활용 및 이진탐색 알고리즘)
     - 29 : 가능한 거리에 대해서 이진탐색으로 가능한 거리 결정
     - 30 : bisect모듈을 사용한 문자 비교 이진 탐색
  - 2021_Dev-match 칫솔판매원 : 이진탐색을 통한 문자 비교
  
  2022.11.09 <16주차 스터디>
  - [이것이 취업을 위한 코딩테스트다] part 3 구현 문제 리뷰
     - 07 : 럭키스트레이트_문자열 조작
     - 09 : 문자열 압축_패턴에 따른 비교 연산
     - 11 : 뱀_deque를 이용한 구현
     - 13 : 치킨배달_조합과 백트래킹

   ~엄청 미뤄졌다..~
  
  2022.12.28 <17주차 스터디>
   - [이것이 취업을 위한 코딩테스트다] part 3 구현 문제 리뷰
     - 15 : visited 번호를 이용한 bfs
     - 17 : 우선순위 큐를 사용한 bfs
     - 19 : dfs로 중복순열 구현
     - 21 : 구현 + bfs
   - programmers
     - 2022_internship_등산코스 정하기 : 다익스트라를 이용한 최적의 경로 찾기

  2023.01.13 <17주차 스터디>
   - [이것이 취업을 위한 코딩테스트다] part 3 다익스트라, 플로이드 워셜
     - 37 : 플로이드 워셜 알고리즘을 이용한 모든 연결 지점에 최단거리 표시
     - 38 : bfs 튜닝 또는 플로이드 워셜을 이용하여 나보다 큰 노드 작은 노드의 수를 계산
     - 39 : 다익스트라를 이용한 최단거리 문제
     - 40 : 다익스트라를 이용한 다양한 정보 구하기

  2023.01.18 <18주차 스터디>
   - [이것이 취업을 위한 코딩테스트다] part 3 그리디 알고리즘
     
  2023.01.25 <19주차 스터디>
   - [BaekJoon Online Judge] DP, Tree

    - 1967_tree dfs를 이용한 tree 지름 구하기
    - 2533_tree dp를 이용한 이차원 문제
    - 1038_combination을 이용한 감소수 아이디어문제
  
   - [Programmers]

    - 귤고르기 : 중복값을 카운트하고 정렬. 입력 값이 크기 때문에 시간복잡도를 고려한 문제해결
    


</div>
</details>
