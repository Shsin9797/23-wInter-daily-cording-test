sentence = input() #문자열 입력
# 모두 소문자로 변경
sentence= sentence.lower()
# 문자열을 순회하며 값을 유니코드 숫자로 바꿔서 리스트에 추가
numlist=[]
for i in sentence:
    num=ord(i)
    if num not in numlist:
        numlist.append(num)


# 모든 알파벳 값이 있는지 확인
numA= ord('a')
numZ=ord('z')
Flag = True

for k in range(numA,numZ+1):
    if k not in numlist:
        #print("N0")
        Flag=False
        break
    #print("YES") 여기다 바로 출력해버리면 .. 반복해서출력됨

if Flag:
    print("YES")
else:
    print("NO")