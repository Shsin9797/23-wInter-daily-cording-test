moveCount = 0 # 이동거리
throw = str(input()) #던진값

#윳의 개수를 세는 부분
aa=0
for a in throw:
    if a =="1":
        aa+=1



#aa 는 윷의 개수
#윷의 개수에 따라 이동거리를 계산하는 부분
if aa == 1:
    moveCount +=1
elif aa== 2:
    moveCount +=2
elif aa==3:
    moveCount +=3
elif aa==4:
    moveCount +=4
elif aa==0:
    moveCount +=5

print(moveCount)