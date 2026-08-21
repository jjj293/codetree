a_math, a_eng=input().split()
b_math, b_eng=input().split()
a_math, a_eng, b_math, b_eng=int(a_math), int(a_eng), int(b_math), int(b_eng)
if a_math==b_math:
    print("A" if a_eng>b_eng else "B")
else:
    print("A" if a_math>b_math else "B")