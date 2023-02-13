"""
T ; 테스트 케이스 수

<< T 만큼 반복 >>
N,M ; 격자 세상크기 ;; N 세로 M 가로

    <<N 만큼 반복 >>
    S  격자세상 한줄씩 제시

                @ : 준식이
                ^ : 가시함정  >> 데미지 +1 씩 카운트
                # : 벽 , 움직일수없음
                . : 길 움직일수있음

K: 입력길이
T1 : 플레이어의 입력

출력 R,C,D  ; 행 ,열,데미지


"""
#준식이 위치알아내는 함수
def findJun(world,N,M):  #인덱스 값이 필요하므로 range 쓴다.
    for q in range(N): #행 인덱스 하나 가져옴 (리스트)
        for w in range(M): #행에서 각 원소 인덱스 하나씩 가져옴
            if world[q][w] == '@' or world[q][w]=='^@': #준식이 / 가시밭에 있는 준식이면
                return q,w #위치 인덱스 반환하고 함수끝



### 준식이 이동하는 함수
def moveJun(world, N,M, t, dem): #t는 사용자 입력값  dem 은 데미지

    # 준식이 위치값 알아내기
    a, b = findJun(world,N,M)

    #t 값에 따라서 준식이 위치 이동시키기
    ## .일때 자리바꾸기 , ^ 있을때 주의 , 범위 벗어나면 아무것도 안일어나도록 해야함..
    try:
        ########################오른쪽 이동 #########################
        if t =='R' : #오른쪽으로 이동하라고하면

            if b+1 >= M: #범위 넘어가면 안움직이고 그대로

                if world[a][b] =='^@': #안움직일때 가시밭에 있으면
                    dem +=1 #데미지 하나 줘야함
                return world,dem
            elif world[a][b+1] =='#': #벽인경우 안움직이고 그대로

                if world[a][b] == '^@':  # 안움직일때 가시밭에 있으면
                    dem += 1  # 데미지 하나 줘야함

                return world, dem



            elif world[a][b+1] =='.': #지나갈수있는곳이면

                if world[a][b] =="@": #준식이만 있던곳이라면
                    world[a][b] = '.' #준식이가 있던곳을 .으로 바꾸고
                elif world[a][b] =="^@": #가시밭 준식이라면
                    world[a][b] = '^' #다시 가시밭으로 바꾼다.


                world[a][b+1] ="@" #준식이를 옮긴다.

                return world,dem


            elif world[a][b+1] =='^': #가시밭이면

                if world[a][b] =="@": #준식이만 있던곳이라면
                    world[a][b] = '.' #준식이가 있던곳을 .으로 바꾸고
                elif world[a][b] =="^@": #가시밭 준식이라면
                    world[a][b] = '^' #다시 가시밭으로 바꾼다.

                world[a][b + 1] = "^@"  # 준식이를 옮긴다.
                dem +=1 #데미지 1 추가한다.

                return world,dem

        #################이동 끝 #################

        ########################왼쪽 이동 #########################
        if t == 'L':  # 왼쪽으로 이동하라고하면

            if b - 1 < 0:  # 범위 넘어가면 안움직이고 그대로

                if world[a][b] == '^@':  # 안움직일때 가시밭에 있으면
                    dem += 1  # 데미지 하나 줘야함

                return world, dem

            elif world[a][b - 1] == '#':  # 벽인경우 안움직이고 그대로

                if world[a][b] == '^@':  # 안움직일때 가시밭에 있으면
                    dem += 1  # 데미지 하나 줘야함

                return world, dem



            elif world[a][b - 1] == '.':  # 지나갈수있는곳이면

                if world[a][b] == "@":  # 준식이만 있던곳이라면
                    world[a][b] = '.'  # 준식이가 있던곳을 .으로 바꾸고
                elif world[a][b] == "^@":  # 가시밭 준식이라면
                    world[a][b] = '^'  # 다시 가시밭으로 바꾼다.

                world[a][b - 1] = "@"  # 준식이를 옮긴다.

                return world, dem


            elif world[a][b - 1] == '^':  # 가시밭이면

                if world[a][b] == "@":  # 준식이만 있던곳이라면
                    world[a][b] = '.'  # 준식이가 있던곳을 .으로 바꾸고
                elif world[a][b] == "^@":  # 가시밭 준식이라면
                    world[a][b] = '^'  # 다시 가시밭으로 바꾼다.

                world[a][b - 1] = "^@"  # 준식이를 옮긴다.
                dem += 1  # 데미지 1 추가한다.

                return world, dem

        #################이동 끝 #################

        ########################아래쪽 이동 #########################
        if t == 'D':  # 아래쪽으로 이동하라고하면

            if a + 1 >= N:  # 범위 넘어가면 안움직이고 그대로

                if world[a][b] == '^@':  # 안움직일때 가시밭에 있으면
                    dem += 1  # 데미지 하나 줘야함

                return world, dem

            elif world[a+1][b] == '#':  # 벽인경우 안움직이고 그대로

                if world[a][b] == '^@':  # 안움직일때 가시밭에 있으면
                    dem += 1  # 데미지 하나 줘야함

                return world, dem



            elif world[a+1][b] == '.':  # 지나갈수있는곳이면

                if world[a][b] == "@":  # 준식이만 있던곳이라면
                    world[a][b] = '.'  # 준식이가 있던곳을 .으로 바꾸고
                elif world[a][b] == "^@":  # 가시밭 준식이라면
                    world[a][b] = '^'  # 다시 가시밭으로 바꾼다.

                world[a+1][b ] = "@"  # 준식이를 옮긴다.

                return world, dem


            elif world[a+1][b] == '^':  # 가시밭이면

                if world[a][b] == "@":  # 준식이만 있던곳이라면
                    world[a][b] = '.'  # 준식이가 있던곳을 .으로 바꾸고
                elif world[a][b] == "^@":  # 가시밭 준식이라면
                    world[a][b] = '^'  # 다시 가시밭으로 바꾼다.

                world[a+1][b] = "^@"  # 준식이를 옮긴다.
                dem += 1  # 데미지 1 추가한다.

                return world, dem

        #################이동 끝 #################

        ########################위쪽 이동 #########################
        if t == 'U':  # 위쪽으로 이동하라고하면

            if a - 1 < 0:  # 범위 넘어가면 안움직이고 그대로

                if world[a][b] == '^@':  # 안움직일때 가시밭에 있으면
                    dem += 1  # 데미지 하나 줘야함

                return world, dem

            elif world[a - 1][b] == '#':  # 벽인경우 안움직이고 그대로

                if world[a][b] == '^@':  # 안움직일때 가시밭에 있으면
                    dem += 1  # 데미지 하나 줘야함

                return world, dem



            elif world[a - 1][b] == '.':  # 지나갈수있는곳이면

                if world[a][b] == "@":  # 준식이만 있던곳이라면
                    world[a][b] = '.'  # 준식이가 있던곳을 .으로 바꾸고
                elif world[a][b] == "^@":  # 가시밭 준식이라면
                    world[a][b] = '^'  # 다시 가시밭으로 바꾼다.

                world[a - 1][b] = "@"  # 준식이를 옮긴다.

                return world, dem


            elif world[a - 1][b] == '^':  # 가시밭이면

                if world[a][b] == "@":  # 준식이만 있던곳이라면
                    world[a][b] = '.'  # 준식이가 있던곳을 .으로 바꾸고
                elif world[a][b] == "^@":  # 가시밭 준식이라면
                    world[a][b] = '^'  # 다시 가시밭으로 바꾼다.

                world[a - 1][b] = "^@"  # 준식이를 옮긴다.
                dem += 1  # 데미지 1 추가한다.

                return world, dem

        #################이동 끝 #################
    except:
        return world, dem
    finally:
        return world,dem





## 테스트시작

#테스트 케이스 받음
T= int(input())

#테스트 케이스만큼 게임 반복
for i in range(T):

    #격자 세상 크기
    N,M = map(int,input().strip().split())

    #격자 세상을 저장할 이중리스트
    world=[]

    #세로길이 N 만큼 반복해서 격자세상을 한줄씩 받아서 리스트로 저장한다.
    for j in range(N):
        P= input()  # input().strip().split()은 띄워쓰기 단위로 끊어서 리스트 만들어줌..
        S=[]
        for l in P:
            S.append(l)

        world.append(S)

    #이용자 입력받는구문
    K = int(input()) #길이
    T1 = input() # 이용자입력값


    dem = 0
    #입력값 반영해서 준식이 위치 변경
    for t in T1: # 값을 하나씩 가져와서 비교하며 위치 변경한다.

        world, dem = moveJun(world, N,M, t, dem) # world 세상과 t 이동값 넣으면 준식이 이동시킨 세상 값, 데미지를 반환해서 반영

    #이동이 끝난 후 준식이 위치 찾아서 받기
    af,bf = findJun(world,N,M)
    print(af+1,bf+1,dem) # 준식이 위치는 1부터시작하는데 인덱스는 0부터 시작하므로 .. +1 씩해줘야함

