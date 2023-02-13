li = map(int,input().strip().split())
li= list(li)
li.sort(reverse=True)

target=[]

while(len(li) != 1):

    a1 = li.pop()
    a2= li.pop()
    partSum= a1+a2
    li.append(partSum)
    li.sort(reverse=True)
    target.append(partSum)

print(sum(target))