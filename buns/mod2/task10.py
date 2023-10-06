a=input()
word=''
for i in range(len(a)):
    if a[i]==' ':
        word+=a[i-1]
print(word + a[-1])