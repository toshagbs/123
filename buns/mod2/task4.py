a=int(input())
if a<0:
    print('Неверный ввод')
else:
    a22=a
    a88=a
    a1616=a
    a2=''
    while a22 > 0:
        a2 = str(a22 % 2) + a2
        a22 = a22 // 2

    a8=''
    while a88 > 0:
        a8 = str(a88 % 8) + a8
        a88 = a88 // 8
    a16=''
    while a1616 > 0:
        a16 = str(a1616 % 16) + a16
        a1616 = a1616 // 16
    print(a2, a8, a16)
