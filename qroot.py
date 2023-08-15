
def pow(a, x):
    p = 1
    for i in range(1, x+1):
        p = p * a
    return p


def fact(n):
    if n == 0:
        return 1
    p = 1
    for i in range(1, n+1):
        p = p * i
    return p


def ncr(n, r):
    return fact(n) // (fact(r) * fact(n-r))


m = -1
l = [1, 1]

for i in range(2, 16):
    v = pow(l[1], i)
    _sum = 0
    t = i // 2
    for x in range(1, t+1):
        _sum = _sum + ncr(i, x) * pow(m, x) * l[i - (x*2)]
    l.append(v - _sum)

l = l[1:]
for i in range(0, len(l)):
    print(l[i], end=",")
print()

for i in range(0, len(l)):
    if i % 2 == 0:
        print(l[i], end=",")
print()
for i in range(0, len(l)):
    if i % 2 == 1:
        print(l[i], end=",")
