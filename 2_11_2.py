N = int(input()) # 빌딩개수
bList= list(map(int,input().strip().split())) # 빌딩 높이 리스트

# 빌딩 높이 계산 하는 구문

#왼쪽에서 보기

lstart = bList[0] # 첫번째 빌딩의 높이
lBCount = 1 # 보이는 빌딩 개수
for i in range(1,N):
    if lstart < bList[i] :
        lBCount +=1
        lstart = bList[i]

#오른쪽에서 보기
rstart = bList[-1] # or N-1 해도됨
rBCount = 1
for j in range(N-2,-1,-1):
    if rstart < bList[j]:
        rBCount +=1
        rstart = bList[j]


#출력
print(lBCount,rBCount)