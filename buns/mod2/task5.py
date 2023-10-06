a=str(input())
n=int(input())
a1=ord(a)
a2=a1+n
a3=chr(a2)
if int(a2)>122:
    a2=a2-122+96
    print(chr(a2))
else:
    print(a3)