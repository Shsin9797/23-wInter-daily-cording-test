#2월 14일 문제 #큐

N = int(input()) # 테스트 개수

queue= []

for i in range(N):
    excute = list(input().strip().split()) # 입력받음

    if excute[0] == 'push':
        queue.append(int(excute[1]))
    else: #pop
        if queue == [] :
            print(-1)
        else:
            print(queue.pop(0))
