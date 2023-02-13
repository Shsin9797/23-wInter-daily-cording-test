# 2월 8일 최대 구간 합
#구간합 가능한 구간의 개수는 N^2 는아니고 ..  1+2+..+ N 까지라서 .. N(N+1) /2 개인듯
#테스트 케이스 한개 충족못함.. .

N =int(input()) # 입력받을 수열길이
nList = list(map(int,input().strip().split())) # 수열 입력받는 부분

#누적합리스트 구하는 부분

sList= []
sum =0

for i in nList:
    sum+=i
    sList.append(sum)


#sList 누적합 리스트를 이용해서 구간합 찾는 부분
#pList =[]
maxS = sList[0] #최댓값을 리스트에 있는 임의 값으로 설정

for L in range(N): #왼쪽 값 #왼쪽값이 천천히 커져야함.. 오른쪽값 먼저 커져야함.. 누적합 구할때 ..
    for R in range(L,N): #오른쪽값 #range 시작값이 왼쪽값 부터 시작해야함..  오안그럼 오른쪽 왼쪽 바뀌어버림
        l= L
        r=R

        #변경코드가 이위에 있으면 안됨. .. 그럼 r이랑 l 비교 자체가 잘못되어버림
        #if (l-1) < 0:
        #    l=1 #for 문 범위가 아예 바뀌어버림.. .  for 문 변수를 바로 쓰지말고 고쳐서 쓰자 ...
            #l을 0으로 두면 안됨.. 1 로 둬야  l-1 했을때 0 나옴


        if r==l: # 이거도 바꿔야함..  l 값은 L 값의 범위에 따라 달라지기 때문
            P= sList[r]
        elif l-1<0:
            P= sList[r]-sList[0]
        else:
            P= sList[r] - sList[l-1]

        #pList.append(P)
        #print(pList)
        #최댓값 확인하는 부분
        if P >maxS :
            maxS=P

#최댓값 출력
print(maxS)


####처음엔 구간합들을 전부 구해서,, 리스트에 넣고.. 그중에서 max 값을 찾으려고 했엇음
# 구간합을 구해서 리스트에 추가하는 부분

# 리스트를 순회하며 max 값 찾는 부분

