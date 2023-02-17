T = int(input()) # 테스트 케이스 개수

#T 번 테스트 수행
for i in range(T):

    N = int(input())  # 수열의 길이
    A = list(map(int, input().strip().split()))  # 수열의 원소 리스트
    A.reverse() # 넣고 뺄때 런타임 줄이기위함


    j=N-1 #마지막 원소를 j 라 두자

    while True:

        if j-1 <0 : #j-1 가 음수가 되면 break (범위 검사 끝)
            break

        elif A[j-1] < A[j] : # A[j-1] 값(뒤에있는값) 이 작아지면.. j-1 번째 삭제 # 부등호 방향 주의.. 디버그로 확인좀 해야할듯..
            A.pop(j-1) # 뭘 pop 하는지 잘보기..
            j = len(A)-1
            #없앴으면  i 값 맨 끝값으로 바꾸고 다시 검사
        else:
            j-=1

    A.reverse()  # 출력하기쉽게 다시 뒤바꿈
    # 출력문
    for t in A:
        print(t, end=" ")
    print()




