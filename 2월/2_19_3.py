#12월5일 최대공약수 구하기
#입력
a,b = map(int,input().strip().split())

def cal(a,b):
    r= a%b   # // 는 정수몫, % 기호가 나머지임!!
    while r != 0:
        a=b
        b=r
        r= a%b

    return b


print(cal(a,b))