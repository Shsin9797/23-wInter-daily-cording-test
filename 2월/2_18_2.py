#파트4 실전문제: 타노스 정렬2
#효율성 높여야한다.. .

T=int(input()) # 테스트 케이스 개수

#타노스 정렬
def ta(N,A):
    Sorted =False
    while not Sorted:
        Sorted =True
        for i in range(N-1):
            if A[i]>A[i+1]:
                A[i] //= 2
                Sorted =False



#출력문
def printList(A):
    for i in A:
        print(i,end=" ")
    print()



# 테스트 시작
for i in range(T):
    N =int(input()) # 수열의 길이
    A = list(map(int,input().strip().split())) # 수열

    #타노스정렬
    ta(N,A)
    printList(A)
