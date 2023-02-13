"""
T 테스트 케이스 개수


반복시작
N,M 2차원 격자 세상의 크기

N: 세로길이
M: 가로길이

S: 격자세상 한줄(N개 나옴)

K: 입력값의 개수
T2: 이동입력값


$$$출력값  >> 반복 끝나고 한번에 출력해도됨
준식이위치 행 열 순서로
"""

##필요한 함수정의

# 준식이의 위치 탐색하는 함수
def findJun(worldLines, N):
    junI1 = 0
    junI2 = 0
    # t 반복문 1
    for t in range(N):  # 줄개수번 만큼 인덱스를 변화시킨다
        # y 반복문 2
        for y in worldLines[t]:  # t번째 줄 리스트에서 값을 하나씩 가져오고.. 거기에 @가 있는지 확인
            # if (y =="@"): #t 줄에 @ 가 있다면
            #     junI = worldLines[t].index('@') #해당 리스트에서 준식이의 위치를 찾는다
            try:
                # 준식이 위치 인덱스 설정하는부분

                junI2 = worldLines[t].index('@')
                junI1 = t  # 위치 조심해야할듯 ?
                break  # y 반복문2 끝
            except:  # @ 가 없는경우 오류발생
                pass

    return junI1, junI2  # 준식이 위치 인덱스 반환


# 준식이 위치이동시키는 함수
def moveJun(worldLines, N,M, T2):
    for t2 in T2:  # 이동키를 하나씩 가져온다.

        # 이동할때마다 준식이 인덱스가 달라지므로.. 계속 다시 호출하기
        # 준식이 위치 인덱스 찾는 함수 호출
        junI1, junI2 = findJun(worldLines, N)



        if t2 == 'R':  # 오른쪽 키 눌렀을때 오른쪽이 #이 아니라면,, . 이라면.. (아무것도 없을수도있으니까.. )준식이위치값을 . 로 바꾸고 준식이 오른쪽 값을 @로 바꾼다..
            try:  # 인덱스값이 오버 뜰수있어서..
                if  (junI2 + 1 >= M):
                    continue
                if worldLines[junI1][junI2 + 1] == '.':
                    worldLines[junI1][junI2] = "."
                    worldLines[junI1][junI2 + 1] = "@"
            except:
                pass
        elif t2 == 'L':  # 왼쪽 키 눌렀을때  . 이라면.. (아무것도 없을수도있으니까.. )준식이위치값을 . 로 바꾸고 준식이 왼쪽 값을 @로 바꾼다..
            try:
                # 음수되면 continue 뜨게
                if  (junI2 - 1 < 0):
                    continue

                if worldLines[junI1][junI2 - 1] == '.':
                    worldLines[junI1][junI2] = "."
                    worldLines[junI1][junI2 - 1] = "@"
            except:
                pass
        elif t2 == "D":  # 아랫쪽 키 눌렀을때  . 이라면.. (아무것도 없을수도있으니까.. )준식이위치값을 . 로 바꾸고 준식이 아래쪽 값을 @로 바꾼다..
            try:
                if (junI1 + 1 >= N) :
                    continue
                if worldLines[junI1 + 1][junI2] == '.':
                    worldLines[junI1][junI2] = "."
                    worldLines[junI1 + 1][junI2] = "@"
            except:
                pass
        elif t2 == "U":  # 위쪽 키 눌렀을때  . 이라면.. (아무것도 없을수도있으니까.. )준식이위치값을 . 로 바꾸고 준식이 위쪽 값을 @로 바꾼다..
            try:
                # 음수되면 continue 뜨게
                if (junI1 - 1 < 0) :
                    continue
                if worldLines[junI1 - 1][junI2] == '.':
                    worldLines[junI1][junI2] = "."
                    worldLines[junI1 - 1][junI2] = "@"
            except:
                pass

    # 검증이 모두 끝난후 준식이의 인덱스를 찾아서 반환한다.
    junIf1, junIf2 = findJun(worldLines, N)
    return junIf1, junIf2


T= int(input()) # 테스트 케이스 개수

fList=[] #최종위치를 저장하는 리스트

for i in range(T):
#테스트 케이스 개수 만큼 반복
#정보 받는 부분
    N,M = map(int,input().strip().split()) # 격자 세상크기  N:세로/ M:가로

    #격자세상 저장할 리스트
    worldLines=[]
    # N번 격자세상 값 받아야함
    for j in range(N):

        world = input()

        line = []
        for h in world:
            line.append(h)

        #line = list(input().strip().split('')) #받은 한줄의 각각의 값을 다 떼어서 리스트로 만든다.
        worldLines.append(line) # 이차원리스트가 생성된다.

    # 이동 키 개수 받기
    K = int(input())
    #이동키 문자 받기
    T2 = input()

    # 정보를 이용해서 준식이 위치를 이동시키는 함수 호출
    i1, i2 = moveJun(worldLines,N,M,T2)
    li1=[i1+1,i2+1]
    #준식이 위치를 리스트에 저장한다.
    fList.append(li1)

#테스트 케이스 반복문이 모두 끝난후 출력
for m in fList: #리스트 하나씩 가져옴
    for n in m:
        print(n,end=" ")
    print()


#준식이의 위치정보를 먼저 받는다
#이동시킨다.
