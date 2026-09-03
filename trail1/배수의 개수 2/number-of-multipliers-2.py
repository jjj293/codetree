arr=[0]*10
cnt=0
for i in range(10):
    arr[i]=int(input())
    if arr[i]%2!=0:
        cnt+=1
print(cnt)