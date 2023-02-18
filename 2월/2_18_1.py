T = int(input()) #테스트 케이스 개수

#타노스 정렬 함수 정의
def ta(A):
    #줄이고 다시처음으로 돌아가야함..
    i=0
    while True:
        if i >= (len(A)-1): #A길이보다 하나 작은거기준확인해야함 .. 아래의 if 문에서 i+1 검사하기때문
            break

        if A[i] >A[i+1]:
            A[i] = A[i]//2
            ta(A) # 재귀함수 호출 (다시처음부터 확인)
        else:
            i+=1

#출력함수 정의
def liPrint(A):
    for i in A:
        print(i,end=" ")
    print()

# T 번 테스트 수행
for i in range(T):
    N = int(input()) # A 의 길이
    A= list(map(int,input().strip().split())) # 수열을 리스트로 받는다

    #타노스 정렬 수행
    ta(A)

    #출력함수
    liPrint(A)







