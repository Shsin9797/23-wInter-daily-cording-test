T =int(input()) #테스트 케이스 개수

#수열 받는 부분
for i in range(T):
    N = int(input()) # 수열의 길이
    aList = list(map(int,input().strip().split()))

    idx =1
    run2=True
    #한칸씩 돌면서 더큰거
    while run2:
        if len(aList)-1 < idx:  # aList 에서 참조하기 전에  len 을 확인해줘야했다...
            break
        elif aList[idx-1] > aList[idx]:
            aList.pop(idx)
            idx=0 #다시 처음부터 돌도록 세팅
        idx+=1



    for t in aList:
        print(t,end=' ')
    print() #다음줄 넘겨주기
