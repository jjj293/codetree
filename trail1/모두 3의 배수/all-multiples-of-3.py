satisfied=True

for _ in range(5):
    n=int(input())
    if n%3!=0:
        satisfied=False
if satisfied==False:
    print(0)
else:
    print(1)
    