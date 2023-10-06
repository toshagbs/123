a=input()
a=a.replace(' ','')
a=a+' '
g='АУОИЭЫЯЮЕЁауоиэыяюеё '
s='БВГДЖЗЙКЛМНПРСТФХЦЧШЩбвгджзйклмнпрстфхцчшщ '
count1=0
count2=0
for i in range(len(a)):
    for e in range(len(g)):
        if a[i]==g[e]:
           count1+=1
        if g[e+1]==' ':
            break
    for l in range(len(s)):
        if a[i] == s[l]:
            count2+=1
        if s[l+1]==' ':
            break

    if a[i + 1] == ' ':
        break
print(count1,count2)