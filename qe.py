co = 0
t = 0
for p in range(1,4):
    for q in range(1,4):
        for c in range(1,4):
            t = t + 1
            D = p*p - 4*q*c
            if D < 0:
                print(p, q, c, D)
                co = co + 1
print(co)
print(t)
