"""
N /곡의 개수
A[1] / 곡이름 N 개 받음
A[2]
A[N]

B[1] /곡의 길이 N개 받음
B[2]
B[N]

M /질문개수
Q[1]  / 질문을 하는시각 N개
Q[2]
Q[M]

"""

#곡의 개수 받음
N=int(input())


#음악리스트
songList =[]
songLength=[]

# 곡의 이름 N 개 받음
for i in range(N):
    song = input()
    songList.append(song)

# 곡의 길이 N 개 받음

length2=0

for k in range(N):

    if k ==0:
        length2 = int(input())
        songLength.append(length2)

    else:
        length1= songLength[k-1]
        length2 = int(input())
        songLength.append(length1 + length2)




# 질문개수
M=int(input())

#질문 받는과정
for t in range(M):
    #몇초 부분의 값을 받을건가요?
    Q = int(input())


    #곡이름 찾는과정

    for i in range(N):
        if Q <= songLength[i]:
            idx = i
            if idx<0 :
                idx=0
            songName= songList[idx]
            print(songName)
            break
