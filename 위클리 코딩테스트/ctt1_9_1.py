import decimal


decimal.getcontext().rounding = decimal.ROUND_HALF_UP


testCase = int(input())
for i in range(testCase):
    N,C= input().strip().split()
    N=int(N)
    if(C =='K'):
        mile= N/1.6


        second = mile%0.1
        #third = mile%0.01
        #mile -=third


        if (second<0.01):
            a= float(decimal.Decimal(str(mile)).quantize(decimal.Decimal("1.0")))
            print(a)
        else:
            a= float(decimal.Decimal(str(mile)).quantize(decimal.Decimal("1.00")))
            print(a)
    else:
        killo=N*1.6
       # second= killo%0.1
       #third = killo % 0.01

        if (second <0.01):
            a=float(decimal.Decimal(str(killo)).quantize(decimal.Decimal("1.0")))
            print(a)
        else:
            a=float(decimal.Decimal(str(killo)).quantize(decimal.Decimal("1.00")))
            print(a)