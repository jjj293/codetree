a, b=input().split()
a, b=int(a), int(b)
i=a
while i<=b:
    print(i, end=' ')
    if i%2==0:
        i+=3
    else:
        i*=2