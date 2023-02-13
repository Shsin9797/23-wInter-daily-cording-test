# 2월 8일 최대 구간 합
#구간합 가능한 구간의 개수는 N^2 는아니고 ..  1+2+..+ N 까지라서 .. N(N+1) /2 개인듯

N =int(input()) # 입력받을 수열길이
nList = list(map(int,input().strip().split())) # 수열 입력받는 부분

#누적합리스트 구하는 부분

sList= []
sum =0

for i in nList:
    sum+=i
    sList.append(sum)


#누적합 sList 를 이용해서 구간합 찾기
maxS = sList[0]

#L이랑 R 구분없이 일단 돌리고 더 큰걸.. R 로 두는게 나을듯..
for a in range(N):
    for b in range(N):

        #L,R 할당 , 작은걸 l에
        if a<b:
            l,r =a,b
        else:
            l,r = b,a

        #
        if r==l:
            P= sList[r]
        elif l-1<0:
            P= sList[r]-sList[0]
        else:
            P= sList[r] - sList[l-1]


        #최댓값 확인하는 부분
        if P > maxS :
            maxS = P

#최댓값 출력
print(maxS)

