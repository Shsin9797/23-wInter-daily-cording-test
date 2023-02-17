N, M = map(int,input().strip().split()) # 돌  개수 , 준식이 행동개수

stone=[]
#돌쌓기
for j in range(N):
    stone.append(j+1)


# 행동 시작

for i in range(M):
    act = input()
    if act == 'raise':
        up = stone.pop(0) # 맨 밑돌 빼기
        stone.append(up) # 다시 끝에 올리기
    else:
        if len(stone) >1:
            stone.pop(0) #맨 밑돌 삭제
        else: # 돌이 하나밖에 안남으면 아무행동 하지 않기
            continue

print(stone.pop(0))

