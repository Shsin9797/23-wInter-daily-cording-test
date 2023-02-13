"""
   T 테스트 케이스 개수
   @ 준식이
   N 1차원 세상의 길이
   M 벽 부술수있는 횟수
   S 문자열
   O 탈출구
   & 몬스터
   # 벽
   . 아무것도없는곳 움직일수있음

   ATK_J 준식이 공격력
   HP_J 준식이 체력

   ATK_M 몬스터 공격력
   HP_M 몬스터 체력

   """

T= int(input()) #테스트 케이스

def search(start,end,step,S,M,ATK_J,HP_J,ATK_M,HP_M):
    count = 0
    # 한칸씩 탐색하는 반복문
    for i in range(start,end,step):

        #마주치는 벽의 개수 구하는 구문
        if S[i] =="#":
            count +=1

        #벽의 개수가 너무 많으면
        if count >M :
            return "fale"
            break

        #몬스터 만났을때
        if S[i]=="&":
            fightFlag = fight(ATK_J,HP_J,ATK_M,HP_M)
            if fightFlag=="lose":
                return "fale"
                break # 해당 방향 탐색종료 ( 실패 )

        # 출구를 만나면 탐색성공
        if S[i] =="O":
            return "sucess"





#탐색시 몬스터 만났을때 싸우는 코드
def fight(ATK_J,HP_J,ATK_M,HP_M):

    #전투 반복문 (전투종료시까지(break 까지) 계속 반복)
    while(True):
        # 몬스터 체력 깎음
        HP_M -= ATK_J

        #몬스터 체력 확인 구문
        if(HP_M <= 0 ):
            return  "win" #이겼음을 반환
            break #전투종료

        #준식이 체력 깎음
        HP_J -= ATK_M

        #준식이 체력 확인 구문
        if(HP_J <=0):
            return "lose" #졌음을 반환
            break #전투종료





#테스트 케이스 만큼 반복
for i in range(T):

    #입력값 설정
    N,M = map(int,input().strip().split()) # N 세상의 길이 & M 벽 부수는 최대횟수
    S= input() #일차원세상
    ATK_J, HP_J = map(int,input().strip().split())
    ATK_M, HP_M = map(int,input().strip().split())


    # 준식이 위치탐색
    idxJun= S.index("@")

    # 준식이 왼쪽 검색 : 탈출가능한지
    searchLeft = search(idxJun,-1,-1,S,M,ATK_J,HP_J,ATK_M,HP_M)


    # 준식이 오른쪽 검색 : 탈출 가능한지
    searchRight = search(idxJun,len(S),1,S,M,ATK_J,HP_J,ATK_M,HP_M)

    if (searchLeft=="sucess" or searchRight=="sucess"):
        print("HAHA!")
    else:
        print("HELP!")






