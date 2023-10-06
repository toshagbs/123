a=str(input())
b = ''
for i in range(len(a)-1,-1,-1):
    if a[i] == '.':
        print(b)
        b= ''
    else:
        b=a[i]+b
print(b)
