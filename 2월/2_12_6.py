###최소값 먼저 찾기
###차이의 절댓값을 더한다

N = int(input())# 길이 입력
numList = list(map(int,input().strip().split()))# 수열 입력

#최소값 찾는부분
min = numList[0]
for i in numList:
    if i < min:
        min =i

#최소값과 요소들의 차이의 절댓값을 sumTime 에 더한다
sumTime = 0
for j in numList:
    diff = abs(min-j)
    sumTime +=diff

print(sumTime)