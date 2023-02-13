#k # 아이폰 개수
#n #가장 높은층
#floor # 안깨지는 최대층
import math
k,n = map(int,input().strip().split())
move=0
#아이폰 개수가 적을때.. 한칸씩 올라가야함.. .
if math.log2(k//3)+2 <=k:
#아이폰 개수가 충분히 많을때
    while (n > 4) :
        n = round(n/2)
        move +=1
    if n >=2:
        print(move+2)
    else:
        print(move+1)

else: #아이폰 개수가 부족할때
    while k !=1:
        n=round(n/2)
        move +=1
        k -=1

    print(move+n)