a = list(map(int,input().strip().split()))
b = list(map(int,input().strip().split()))

count=len(a)

#덧셈출력
for c,d in zip(a,b):
    if count %2 !=0:
        count -= 1
        continue
    if c+d ==0:
        continue
    count-=1
    print(c+d,count//2,end=" ")


"""    if count %2 !=0 :
        print(c,end=" ")
        count-=1
        continue
    count-=1
    print(c+d,end=' ')"""

print()

#뺄셈 출력
count=len(a)
for c,d in zip(a,b):
    if count %2 !=0:
        count -= 1

        continue
    if c-d ==0:
        print("   ",end=" ")
        continue
    count-=1
    print(c-d,count//2,end=" ")

'''    if count %2 !=0 :

        print(c, end=" ")
        count-=1
        continue
    count-=1
    print(c-d,end=' ')'''
print()