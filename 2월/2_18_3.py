#타노스 정렬 2 시간 단축시키기
T= int(input()) #테스트 케이스 개수


# 바뀌면 뒤에꺼랑 비교하도록.. 재귀 구현

#타노스 정렬 구현
def ts(N,A):
    Sorted =False
    while not Sorted:
        Sorted =True
        for i in range(N):
            if A[i] >A[i+1]:
                A[i] //= 2
                Sorted =False

        


#출력문 구현
def printList(A):
    for i in A:
        print(i,end=" ")
    print()



# 테스트 반복
for i in range(T):
    N= int(input()) # 수열의길이

    A= list(map(int,input().strip().split())) # 수열 리스트

    ts(N,A) #타노스 정렬
    printList(A) #출력