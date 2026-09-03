a, b=input().split()
a, b=int(a), int(b)
mul=1
for i in range(1, b+1):
    if i%a==0:
        mul*=i
print(mul)