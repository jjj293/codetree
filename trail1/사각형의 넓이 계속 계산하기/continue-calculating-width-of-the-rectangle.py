while True:
    arr=[0]*3
    arr=input().split()
    arr[0], arr[1]=int(arr[0]), int(arr[1])
    print(arr[0]*arr[1])
    if arr[2]=='C':
        break


