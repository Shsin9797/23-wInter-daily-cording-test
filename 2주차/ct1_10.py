"""
T 테스트 케이스 개수
N 문자열의 길이
S 주어진 문자열
A,B 정수. A 부터 B 까지 범위의 문자열을 확인해보겠다.
"""

T =int(input())
for i in range(T):
    #기본 입력을 받는 구문
    N = int(input())
    S=input()
    A,B= map(int,input().strip().split())
    flag=False
    #첫번째글자가 U인지 확인하는 구문
    if S[A-1] == 'U':

        count=0
        # m 만 있는지 확인하는 구문
        for i in range(A,B):
            if S[i] != "m":
                flag = False
                break
            count+=1
            if(count>=2):
                flag = True

    if flag == True:
        print("YES")
    else:
        print("NO")