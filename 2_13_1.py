# 2월 7일  누적합

N = int(input()) #입력값 개수
nList = list(map(int,input().strip().split()))
sList=[]
sum=0

#누적합 리스트 생성
for i in nList:
    sum+=i
    sList.append(sum)

#출력

for k in sList:
    print(k,end=" ") #띄워쓰기 해야함
print()