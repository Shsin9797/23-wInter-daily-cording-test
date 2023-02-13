
T = int(input())
for i in range(T):
    N = int(input()) # 수열의 길이
    suyeal = list(map(int,input().strip().split()))
    dif = suyeal[0]
    for t in range(2,N):
        if (dif != suyeal[t-1]) and (dif != suyeal[t]):# dif != [t ]  라고 적어서 틀렸음
            break
        elif dif != suyeal[t-1]:
            dif=suyeal[t-1]
            break  # 값 바뀌면 break 해야됨.. 찾은거라서 ..
        elif dif != suyeal[t]:
            dif= suyeal[t]
            break

    j= suyeal.index(dif)
    print(j+1)