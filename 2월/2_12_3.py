S = input().lower() # 입력받고 다 소문자로바꿈

codeList = []
# S 값을 순회하며 유니코드 숫자로 바꾸고 / 리스트에 없으면  추가
for i in S:
    num = ord(i)
    if num not in codeList:
        codeList.append(num)


#리포그램인지 확인하는 구문
numA = ord('a')
numZ = ord('z')

#없는 문자를 넣을 리스트
noAlpha = []
# 리포그램인지확인하는 깃발
isLifo = False

for j in range(numA,numZ+1):
    if j not in codeList: # 값이 없으면
        isLifo =True
        alph = chr(j) #문자로 다시바꿔서
        noAlpha.append(alph) #리스트에추가


if isLifo :
    print("YES")
    for t in noAlpha:
        print(t,end="")
    print()
else:
    print("NO")