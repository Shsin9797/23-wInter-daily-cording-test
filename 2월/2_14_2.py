T =int(input()) #테스트 케이스 개수
for i in range(T):
    N = int(input()) # 수열의 길이
    aList = list(map(int,input().strip().split()))
  #  bList = aList.copy() # 복제





    """for j in range(1,N):
        if aList[j-1] > aList[j]:
            #aList.pop(j) # 바로 pop 하면 ..aList 길이가 줄어들어서.. 안됨. .
            bList[j] = 'Null'"""



idx =1
run2=True
while run2:

    if aList[idx-1] > aList[idx]:
        aList.pop(idx)
        idx=0
    idx+=1
    if len(aList)-1 < idx:
        break


for t in aList:
    print(t,end=' ')
