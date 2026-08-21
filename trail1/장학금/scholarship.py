m, f=input().split()
m, f=int(m), int(f)
if m<90:
    print(0)
else:
    if f>=95:
        print(100000)
    elif f>=90:
        print(50000)
    else:
        print(0)