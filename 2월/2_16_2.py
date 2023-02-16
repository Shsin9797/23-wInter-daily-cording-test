book = input()  #String 형으로 받음
N = len(book)
M = int(input())  # 행동 개수

left = []
right = []

#초기 세팅
for i in range(N-1,-1,-1): #초기세팅 주의
    if i ==0:
        left.append(book[i]) # 뭘 추가할건지 적어줘야함
    else:
        right.append(book[i])


#수행
for t in range(M):
    a, b = input().strip().split() #strip(), split() 적어줘야함.. & map함수는 각각의 값에 함수적용할때 쓰는거라.. 여기선 필요없음
    if a =='move' and b=='right':
        if len(right) <=1:
            continue
        else:
            swap = right.pop()
            left.append(swap)

    elif a =='move' and b=='left':
        if len(left) <=1:
            continue
        else:
            swap = left.pop()
            right.append(swap)

    elif a=='tear' and b=='right':
        if len(right) <=1:
            continue
        else:
            right.pop()


    elif a == 'tear' and b=='left':
        if len(left) <=1:
            continue
        else:
            left.pop()


#출력
print(left.pop(), right.pop())