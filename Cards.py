import math


def fn(n, width):
    s = str(n)
    r = width - len(s)
    for i in range(r):
        s = "0" + s
    return s


def allow(s, l):
    for c in s:
        if int(c) not in l:
            return False
    return True


def cal(width):
    d = {}
    x = ""
    for i in range(width):
        x = x + "5"
    for i in range(0, int(x) + 1):
        s = fn(i, width)
        c = [0, 1, 2, 3, 4, 5]
        p = [1, 5, 10, 10, 5, 1]

        if allow(s, c):
            ls = 0
            ps = 1
            for c in s:
                v = int(c)
                ps = ps * p[v]
                ls = ls + v
            if d.get(ls) is None:
                d[ls] = 0
            d[ls] = d[ls] + ps
            #print(s, ls , ps)

    _s = 0
    for k, v in d.items():
        _s = _s + k * d[k]
    print(d)
    print(_s)
    print(_s / math.pow(32, width))


for i in range(1, 7):
    print(i)
    cal(i)
    print("-------------------")