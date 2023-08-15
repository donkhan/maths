
def mult(a, b):
    s = 0
    for t in zip(a, b):
        s = s + t[0] * t[1]
    return s


def mul(a, b):
    r = []
    for x in range(0, len(b[i])):
        c = []
        for y in range(0, len(a)):
            c.append(b[y][x])
        r.append(mult(a, c))
    return r


a = [
    [1, 2, 3],
    [3, 4, 5]
]

b = [
    [4, 2],
    [6, 1],
    [3, 5]
]

r = []
for i in range(0, len(a)):
    r.append(mul(a[i], b))

print(r)
