

###T번 반복안해서 틀린 케이스

T = int(input()) # 테스트 케이스 개수
N = int(input()) # 수열의 길이
A=list(map(int,input().strip().split())) #수열의 원소 리스트


Sorted=False
i=1
while not Sorted: #정렬되지 않은경우 아래 반복문 계속

    #i를 변경해가며 정렬확인하는 반복문
    if A[i-1] >A[i]:
        A.pop(i) #제거
        #제거 됐으면 그냥 그 i 값 그대로 다시 반복 시작

    else: # i번째 정렬이 잘 되어있다면
        if i < len(A)-1:
            i+=1 #다음번 체크
        else: #범위넘으면
            Sorted =True # 둘다할필요 없긴한듯 둘중하나만 해도 될듯
            break


#출력문
for j in A:
    print(j,end=" ")
print()

##시간초과 뜨는게.. 리스트가 하나씩 앞으로 당겨와서 그런거인듯..
