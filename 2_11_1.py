N= int(input()) #사람의 수
mList =  list(map(int,input().strip().split()))

#사람 선택하는 외부 반복문
for i in range(N):
    refer = mList[i] # 얘가 비교대상
    bigger,smaller =0,0 # 값 초기화
    #돌아가며 돈 비교하는 내부 반복문
    for j in range(N):
        if mList[j] > refer :
            bigger +=1
        elif mList[j] <refer:
            smaller +=1
    #비교가 끝나면 출력
    print(smaller,bigger)