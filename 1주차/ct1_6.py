T = int(input());

for i in range(T):
    N,M = map(int,input().strip().split()) #N : 세상의길이 M 부술수있는 문의 수
    S=input() #문자열

    #준식이(@) 위치 먼저 찾고
    idx= S.index("@")


    #그 앞뒤로 M 만큼 탐색해서 O 나 G 가 있으면 탈출가능 상태로 전환
    canEscape = False # 탈출 여부 확인 하는 코드

    # 마이너스 됐을때 어케처리할거냐..
    a = (lambda :(idx-M-1) if ((idx-M-1)>=0) else 0)()

    # +1의 위치 주의
    #b= (idx+M+1)%N+1 # 최대길이 N이 5 이고  M이 0인경우.. M+1 = 5됨.. 0+1 되어서 1 되니까. .처음으로 돌아가버림..
    #그렇다고 b =(idx+M)%N+2 하면 또 범위 오바해버림..

    b= (lambda : idx+M+2 if (idx+M+2 < N) else N )()


    # a, b 크기 비교해서 작은걸 a 해줘야함.. 안그러면 range 구문 안돌아감
    # a,b= (b,a if a<b else a,b) 조건식? A:B 구문 이런거 안되는지...
    """if(a>b):
        a,b=b,a
    else:
        a,b=a,b"""





    for i in range(a,b): #파이썬은 음수 인덱스도 허용하기때문에 마이너스가 안되게 해야함... 절댓값 쓰기.. .

        if(S[i] =="O"):
            canEscape=True
            break; #탈출여부 찾았으니 break 해주기 범위넘어갈수있으므로 break 해줘야함..
        elif(S[i]=="G"):
            canEscape=True
            break;

    #탈출 가능하면 HAHA! 출력
    if(canEscape):
        print("HAHA!")
    else:
        print("HELP!")


