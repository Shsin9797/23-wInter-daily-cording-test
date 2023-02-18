#파트4 실전문제: 타노스 정렬2
#효율성 높여야한다.. .

T=int(input()) # 테스트 케이스 개수

#타노스 정렬
def ta(A):
    i=0
    while True:
        if i+1 >= len(A): # 같아도 안됨 인덱스는 하나작은거까지 있으므로
            break
        elif A[i]>A[i+1]:
            A[i] //= 2
            ta(A) #재귀함수 호출로 i=0 부터 다시 체크
        else:
            i+=1


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
    ta(A)
    printList(A)
