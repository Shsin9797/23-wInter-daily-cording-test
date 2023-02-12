#행 이 같으면  0번
#행이 다르고 열이 다르면 1번


inputList = list(map(int,input().strip().split())) #입력받기
x1,y1,x2,y2 = inputList #언패킹

if (x1 == x2) or (y1 == y2):
    print(0)
else:
    print(1)