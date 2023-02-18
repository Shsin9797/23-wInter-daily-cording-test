#타노스 정렬 2 시간 단축시키기
T= int(input()) #테스트 케이스 개수


#이중 for 문을 이용하여
#타노스 정렬 구현
def ts(N,A):
    for i in range(N):
        for j in range(N):
            if i>j :
                a,b =j,i
            else:
                a,b= i,j

            if A[a] > A[b]:
                A[a] //=2



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