a=input()
count=0
for i in range(len(a)):
    for k in range(len(a)):
        if a[i]==a[k] and i!=k:
            count+=1
if count>0:
    print(True)
else:
    print(False)