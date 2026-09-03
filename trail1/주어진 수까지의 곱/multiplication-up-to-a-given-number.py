a, b=input().split()
a, b=int(a), int(b)
mul=1
for i in range(a, b+1):
    mul*=i
print(mul)