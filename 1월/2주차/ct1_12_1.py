"""
T 테스트 케이스의 개수

N 테슬라 주가가 주어질 일 수 ###(마지막 날)
M 이가격 만큼 올라가면 바로 판다
K 테슬라 구매한 날의 번째수 ######

JB 못팔면 이거 출력

T
N M K
A[1], A[2], ... 테슬라 가격

"""
#테스트 케이스 개수

def main():
    T = int(input())

    for t in range(T):

        #입력 받는구간
        # 주가 개수 N /팔 가격 M / 주식 산 날 K
        N,M,K = map(int, input().strip().split())
        A= list(map(int,input().strip().split()))

        #계산하는 구간
        sellStock(A,N,M,K)



#계산함수  N 번째 날에 사서(인덱스는 -1) 하나씩 차례로 순회하다가 해당 값이 M 이 넘어가면 팔고 해당 번째를 출력
#끝까지 가도 없으면 JB  출력
def sellStock(A, N,M,K):

    #산가격
    buy=A[K-1]
                # 산날 ~ 끝까지 순회
    for i in range(K-1,N):

        if A[i] >= M+buy :
            print(i+1)
            break

        if i ==N-1:
            print("JB")
            break



main()