# 12월 2일 재귀 피보나치

N = int(input())

def fibo(N):

    if N==0:
        return 0
    elif N==1:
        return 1

    return fibo(N-1)+fibo(N-2)

#실행 << 출력문 빼먹지 말기.. 위엔 그냥 함수만정의한거임
print(fibo(N))