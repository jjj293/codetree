a_con, a_tem=input().split()
b_con, b_tem=input().split()
c_con, c_tem=input().split()
a_tem, b_tem, c_tem=int(a_tem), int(b_tem), int(c_tem)
cnt=0
if a_con=='Y' and a_tem>=37:
    cnt+=1
if b_con=='Y' and b_tem>=37:
    cnt+=1
if c_con=='Y' and c_tem>=37:
    cnt+=1
if cnt>=2:
    print("E")
else:
    print("N")
