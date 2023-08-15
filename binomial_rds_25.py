

def ncr(n, r):
    num = 1
    for i in range(n, n-r,-1):
        num = num * i
    den = 1
    for i in range(1, r+1):
        den = den * i

    #print(num, den)
    return num / den

print(ncr(9,5))
v = 0
for i in range(21, 31):
    v = v + ncr(i, 5)
print(v)

for i in range(0,10):
    print(ncr(22,i))
print(ncr(31,6) - ncr(21,6))



print(ncr(21,5) + ncr(22,5))
print(ncr(23,6) - ncr(21,6))