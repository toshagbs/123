a = input()
w = 0
q = 0
for i in a:
    if i == '1':
        q += 1
    elif i == '0':
        w += 1
if q == w:
    print('yes')
else:
    print('no')