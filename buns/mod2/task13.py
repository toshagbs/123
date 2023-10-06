a=int(input())
sum_chet=0
sum_nechet=0
while a>0:
    if len(str(a))%2==0:
        sum_chet+=a%10
    else:
        sum_nechet+=a%10
    a=a//10
if (sum_chet*3+sum_nechet)%10==0:
    print('yup')
else:
    print('nope')