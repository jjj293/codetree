a, b, c=input().split()
a, b, c=int(a), int(b), int(c)
if a>=b and a>=c:
    print(a)
else:
    if b>=c:
        print(b)
    else:
        print(c)