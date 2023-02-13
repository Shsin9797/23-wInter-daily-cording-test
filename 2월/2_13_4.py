#2월 13일 코테  #스택
N = int(input()) #연산의 개수

stack = []

#연산 N번 수행
for i in range(N):
    excute= list(input().strip().split())
    # 첫번째는 push/pop 결정 두번째는 어떤숫자를 할것인지



    if excute[0] == 'push':
        stack.append(int(excute[-1]))

    elif excute[0] =='pop':
        if stack == [] : #비어있다면
            print('-1')
        else:
            print(stack.pop(-1))