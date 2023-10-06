a=input()
a=a.replace(',','')
b=a[-1]
a=a+' '
count=0
for i in range (len(a)):
    if a[i]==b:
        count+=1
    if a[i]==b and a[i+1]!=b or a[i+1]==' ':
    #elif count!=0 and i!=b:
        break
print(count)

