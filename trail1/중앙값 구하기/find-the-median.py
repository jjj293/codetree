a, b, c=input().split()
a, b, c=int(a), int(b), int(c)
if (b>a and a>c) or (c>a and a>b):
    print(a)
elif (a>b and b>c) or (c>b and b>a):
    print(b)
else:
    print(c)