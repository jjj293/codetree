n=int(input())
i=1
while i<=n:
    if i%3==0 or ((i%10)%3==0 and i%10!=0) or ((i//10)%3==0 and i//10!=0):
        print(0, end=' ')
    else:
        print(i, end=' ')
    i+=1