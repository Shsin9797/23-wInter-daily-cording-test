"""
노래를 반복해서 듣는다!!
N: 노래개수

N번 노래를 받음
N 개의    A[i] i번째 노래이름 1~20
N개의     B[i] i 번째 노래의 길이 1~300

M 질문의 개수
M 개의      Q[i] 질문을 하는 초
"""

#노래길이 비교하고 출력하는 함수 정의
def compareSong(N, A, B, Q, M):  # 노래개수 / 노래이름 / 노래길이 / 질문시각 / 질문개수

    # 반복문 돌때마다 값을 더해야함

    sumofSong = 0  # 곡들의 길이

    idx = 0  # B 에서 값을 하나씩 가져올때 인덱스 사용함( 인덱스를 반환할거라 인덱스 알아야함 )

    for i in range(M):  # 질문개수만큼 출력

        sumofSong += B[idx]  # 노래의 길이합 구하기

        if Q <= sumofSong:  # 질문한 시각이 노래의 길이 보다 작거나 같으면
            print(A[idx])  # 해당곡 출력하고 반복문 종료
            break

        idx += 1  # 인덱스값을 1 증가시켜줌 (다음곡 구할때 쓰게 )
        if idx >= N:  # 인덱스값이 범위를 초과하면
            idx = 0  # 0으로 초기화 하고 다시 시작


#노래 개수 받음
N= int(input())

#N번 반복하며 노래 이름 받음

A=[] #노래 이름 저장소
for i in range(N):
    a=input()
    A.append(a)

#N번 반복하며 노래 길이 받음

B=[] #노래 길이 저장소
for i in range(N):
    b= int(input())
    B.append(b)


M = int(input()) #질문개수 받음

#질문받고 해당 시각의 노래 출력하는 구문
for i in range(M):
    Q= int(input())

    #시간비교
    compareSong(N,A,B,Q,M)





