#2월 21일 [하] [그래프] 인접 리스트

N,M =map(int,input().strip().split())  #정점개수, 간선개수
# 빈 정점리스트 구현
adj = [[] for i in range(N+1)]

# 넣기
for j in range(M):
    U,V = map(int,input().strip().split())
    adj[U].append(V)
    adj[V].append(U)



#출력 ## 출력문 주의
for k in range(1,N+1):
    adj[k].sort() #오름차순 정렬하기
    if adj[k] : # 비지않았다면
        for t in range(len(adj[k])):    #이부분 넣어줘야 리스트 내부의 값들 하나씩 가져올수잇음
            print(adj[k][t],end=" ")
        print()
    else:
        print(-1)
