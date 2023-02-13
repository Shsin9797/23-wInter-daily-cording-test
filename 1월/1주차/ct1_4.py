s= input()
count =0

for i in s:
    if(i == '#'):
        count +=1


if (count >=2):
    print("HELP!")
else:
    print('HAHA!')
