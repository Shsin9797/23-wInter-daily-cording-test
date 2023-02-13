N,M = map(int, input().strip().split())  # N : 수열의 길이 , M : 테스트케이스 개수

# 수열 입력받음
numList = list(map(int,input().strip().split()))

# 테스트를 M 번진행
for i in range(M):
    L,R = map(int,input().strip().split())

    sumNum=0 # 합 초기화
    #합하는 부분
    for k in range(L-1,R): # -1 해주는거 조심 , R 에는 - 안해도됨.. R까지 어차피 안감
        sumNum += numList[k]

    print(sumNum)