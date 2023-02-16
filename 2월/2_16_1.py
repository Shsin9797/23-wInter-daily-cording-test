S = input() #리스트로 할필요 없었음.. .split() 하면 리스트로 나옴..

gal = []
isCor=True

for i in S:
    if i == '(': #여는 괄호라면
        gal.append(i)
    elif i == ')':
        if not gal: # 비어있다면
            isCor=False
            break # false 인거 알게되면 반복문 멈춰야함
        elif gal.pop() =="(":
            continue
        else:
            isCor = False
            break

if isCor:
    print('YES')
else:
    print('NO')