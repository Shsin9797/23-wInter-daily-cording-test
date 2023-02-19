T= int(input()) # 테스트 케이스 개수

#Umm문자열 확인함수 정의
def countUm(N,S,A,B,count):
    for t in range(A,B+1):
        if S[t] == "U" and (t+1) < N: # U로 시작하면 이제 m 만있는지 확인시작
            isUmm=True
            for k in range(t,B+1):
                if k != "m":
                    isUmm=False
                    break
        if isUmm:
            count+=1
    return count;





    return count;

for i in range(T):
    N,M =map(int,input().strip().split()) #N:문자열길이 M:관찰횟수
    S = input()

    #테스트 시작
    for j in range(M):
        A,B= map(int,input().strip().split())

        count =0

        #Umm문자열 확인 함수 호출
        addcount =