N = int(input()) # 초밥 개수
susiList= list(map(int,input().strip().split())) # 초밥리스트 받는 구문

BM= 320  # 기준 개수

# 하나씩 비교해보며 얼마나 차이나는지 확인하고
# 차이가 더 적다면 선택값을 변경

close = susiList[0] # 첫번째를 선택

#차이를 구해주는 함수 정의
def gap(a,BM=320):
    gap = abs( BM - a)
    return gap

# 가장가까운값 찾기
for j in susiList:  #susiList[j] 쓸필요없음.. 자체에 이미 들어있음
    if gap(j) < gap(close) : #갭이 더작다면
        close = j # 가장 가까운값 변경

#찾은 close 의  인덱스값+1 출력
print(susiList.index(close) +1)
