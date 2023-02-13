"""
N 질문의개수
A,B 곱 구할 두 정수

"""
#최소 공배수 구하는 함수 정의
def findBe(A,B):

    #최대 공약수 구성요소를 저장할 리스트 목록
    liY = []

    #나누어떨어지는지 확인하는 깃발
    Flag= True

    #나누어떨어지지 않을때까지 도는 반복문
    while Flag:

        #작은수를 A 에 세팅
        if A > B:
            A,B= B,A
        
        if A==1 or B==1: # 이경우, for 반복문이 아예돌지 않기때문에 while  반복문 정지해줘야함
            break 
        
        # 2부터 작은수A까지 나누는 수 변경 해가며 나눠보는 for 문
        for i in range(2,A+1): #1하면 무조건 나누어떨어짐.. 2부터해야함..

            #나누어떨어지는경우
            if(A%i==0 and B%i==0): # 둘다 나누어떨어진다면..

                #A,B 값을 몫으로 변경 (줄여준다.)
                A= A//i
                B= B//i

                #나눈 i 를 리스트에 저장(나중에 다 곱할것임)
                liY.append(i)
                break #for 반복문 중단

            #나누어떨어지는 i 값을 못찾은경우 (i가 A값이 되어버린경우)
            if i ==A:
                Flag = False #깃발을 False 로 바꾼다. >> while 반복문이 끝나게 된다.
                break #for 반복문 중단

        #최소공배수를 구하는 구간

        #리스트값들 다곱하고 거기에 A,B 값도 곱한다.
    Gop=1
    for k in liY:
        Gop*=k

    Gop *=A
    Gop *=B

    return Gop #최소공배수를 반환한다.


#테스트 개수 받음
N = int(input())

#테스트 값들 받음
for i in range(N):
    A,B =map(int,input().strip().split())

    #최소공배수와 곱이 같은지 확인하는 구문
   # print(A)
   # print(B)



    #최소공배수
    gong = findBe(A,B)

    # 곱
    gop = A * B


   # print(gong)
   # print(gop)

    if gong == gop: # 공배수와 곱이 같다면
        print("Perfect")
    else: #공배수와 곱이 다르다면
        print("Not even close")



