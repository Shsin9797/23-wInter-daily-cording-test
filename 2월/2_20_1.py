# 2월 20일 문제 #인접행렬

N,M =map(int,input().strip().split())  # 정점개수 N , 간선의 개수 M

adj=[]

#빈 인접행렬 생성  ( 2차원 행렬 초기화)
for k in range(N):
    adj+=[[0]*N]




# M개 간선 받아오기 (U,V) 점 U 와 V 를 이음
for i in range(M):
    U,V=map(int,input().strip().split())
       # 범위 주의.. -1 붙이기 1부터시작하는 건데 인덱스는 0부터 시작하니까..
    adj[U-1][V-1] = 1
    adj[V - 1][U - 1] = 1 #자리바꾼거도 1로 만들어 줘야함

# 그래프 인접 행렬 출력하기
for y in adj:
    for x in y:
        print(x,end=" ")
    print()