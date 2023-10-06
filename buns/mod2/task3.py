a, b, c = (c for c in input() if c != ' ')
if 1000<=a<=-1000 or 1000<=b<=-1000 or 1000<=c<=-1000:
    print(0)
elif a<=b<=c or c<=b<=a:
    print(b)
elif b<=a<=c or c<=a<=b:
    print(a)
elif a<=c<=b or b<=c<=a:
    print(c)