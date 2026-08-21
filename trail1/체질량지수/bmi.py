h, w=input().split()
h=int(h)
w=int(w)
b=w//((h/100)**2)
print(int(b))
if b>=25:
    print("Obesity")