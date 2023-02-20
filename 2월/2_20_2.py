# 12월 6일 뒤집어도 같은수


# 1-1,8-8 #0 도검사해야함 // 6<->9 (가운데있으면 안됨)
# 짝수 홀수 나눠서 검사


#찾는 함수 정의
def isReverseNum(N,SN):
    isFit = True

    #짝수 개수인경우(2,4,6,8)
    if N%2==0:
        e = N // 2
        for i in range(1,e+1):
            if SN[i-1]  not in ['1','8','6','9','0']: # 이조건 없으면 ,,
                isFit=False
                break
            elif SN[i-1] == "1":
                if SN[-i] !="1":
                    isFit=False
                    break

            elif SN[i-1] == "8":
                if SN[-i] != "8":
                    isFit = False
                    break
            elif SN[i -1] == "6":
                if SN[-i] != "9":
                    isFit = False
                    break

            elif SN[i - 1] == "9":
                if SN[-i] != "6":
                    isFit = False
                    break
            elif SN[i - 1] == "0":
                if SN[-i] != "0":
                    isFit = False
                    break


    #홀수 개수인경우(3,5,7,9)
    else:
        e = (N // 2)+1
        for i in range(1, e +1 ): #e+1 맞음.. i-1 찾을거라..
            #중간값이 이거에 해당안되면
            if SN[e-1] not in ['1','8','0']:  # 주의 .. SN[i-1]  아님.. e+1 도 아님 SN[e+1] 도아님 여긴 S[e] 도 아님 S[e-1임 #0 도검사해야함
                isFit= False
                break
            if SN[i-1] not in ['1','8','6','9','0']: #이조건도 필요함..
                isFit = False
                break

            if SN[i - 1] == "1":
                if SN[-i] != "1":
                    isFit = False
                    break

            elif SN[i - 1] == "8":
                if SN[-i] != "8":
                    isFit = False
                    break
            elif SN[i - 1] == "6":
                if SN[-i] != "9":
                    isFit = False
                    break

            elif SN[i - 1] == "9":
                if SN[-i] != "6":
                    isFit = False
                    break
            elif SN[i - 1] == "0":
                if SN[-i] != "0":
                    isFit = False
                    break

    return isFit


#숫자 세기
def main():
    N = int(input()) # 2자리수 ~ 9자리수
    count =0 # 개수세는 변수

    #범위 변수 만들기 # 근데 저위에있는 수를 무작위로 넣어도 되긴할듯..randInt(1,8,9,6) 해서..
    a = 10**(N-1)
    b =  10**N  # -1 도 안해도됨
    for i in range(a,b):
        SN = str(i)
        if isReverseNum(N,SN):
            count+=1

    print(count)




main() # 메인함수 호출
