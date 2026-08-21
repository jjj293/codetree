a, b, c=input().split()
a=int(a)
b=int(b)
c=int(c)
min=a
if min>b:
    min=b
if min>c:
    min=c

if min==a:
    print(1, end=' ')
else:
    print(0, end=' ')
if a==b and b==c:
    print(1)
else:
    print(0)