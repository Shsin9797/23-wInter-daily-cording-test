#12월 7일 Anagram 판별

a,b= input().strip().split() # 문자열 입력받기

#애니어그램 확인
isAna=True
for i in a: # 한개씩 떼어서
    if i not in b:
        isAna=False
        break

if isAna:
    print("True")
else:
    print("False")