#2월 9일 알파벳 빈도  ## 문자값을 숫자로 변경해서 계산하기 더 편하게 할수도있구나..

N,M = map(int,input().strip().split()) #N: 문자열 길이  M: 테스트 개수
S= input() # 문자열 받기

eCollector=[]

#문자열 값을 떼어내서 e 면 1을 리스트에 추가한다.
for i in S:
    if i =='e':
        eCollector.append(1)
    else:
        eCollector.append(0)

#L,R 받는구문 // M번 반복
for test in range(M):
    L,R= map(int,input().strip().split())
    # L부터 R 까지 e 개수 구해서 출력
    eNum= sum(eCollector[L-1:R])
    print(eNum) # 출력하는거 까먹지말기
