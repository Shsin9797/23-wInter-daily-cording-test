T = int(input()) #테스트 케이스 개수

for i in range(T):
    N = int(input())  # 대여소의 개수
    aList = list(map(int,input().strip().split())) #대여소의 자전거
    M = int(input()) # 이용기록의 개수

    # 타슈이용기록 U 빌린곳 V 반납한곳
    for j in range(M):
        U,V = map(int,input().strip().split())
        aList[U-1] -=1
        aList[V-1] +=1

    #대여소 타슈 개수 출력
    for y in aList:
        print(y,end=" ")
    print()





