
T=int(input())

#테스트를 T번 진행하는 반복문
for i in range(T):
    count = 0
    N, M = map(int, input().strip().split())
    S = input()

    #준식이와 문의 위치를 확인해야함
    placeOfJ =S.index('@') #준식이의 위치를 찾는다

    placeOfO=S.index('O') #출구의 위치를 찾는다.


    #해당위치 사이에 있는 문의 개수를 센다.
    #벽의 개수를 세는 반복문
    if (placeOfO > placeOfJ): # 출입구가 오른쪽에 있다면
        for q in range(placeOfJ,placeOfO+1): #준식이와 출입구 사이이의 인덱스를 이용해서
            k=S[q]    # 해당 문자를추출
            if (k== "#"): #k 값이 '#' 과 같다면 ( 이때 # 을 문자열 처리해줘야함에 주의 파이썬은  자바가 아니라서 ' 랑 " 구분없음  )
                count +=1 # 벽의 개수를 하나씩 증가시켜준다.
    else: #출입구가 왼쪽에 있다면
        for p in range(placeOfJ,placeOfO-1,-1): #준식이와 출입구 사이이의 인덱스를 이용해서
            k=S[p]    # 해당 문자를추출
            if (k== "#"): #k 값이 '#' 과 같다면 ( 이때 # 을 문자열 처리해줘야함에 주의 파이썬은  자바가 아니라서 ' 랑 " 구분없음  )
                count +=1 # 벽의 개수를 하나씩 증가시켜준다.
    if(count > M):  #벽의 개수가 최대로 부술수있는 횟수보다 큰경우
        print("HELP!")
    else:
        print("HAHA!")