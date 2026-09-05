sum=0
cnt=0
while True:
    age=int(input())
    if age//10!=2:
        aver=sum/cnt
        print(f"{aver:.2f}")
        break
    sum+=age
    cnt+=1


    