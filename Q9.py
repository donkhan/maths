import math


def fact(n):
    p = 1
    for i in range(1,n+1):
        p = p * i
    return p


def ncr(n, r):
    return fact(n) / (fact(r) * fact(n-r))


def women_selection():
    men = 8
    women = 12
    selected = 5

    e = 0
    for i in range(0, selected+1):
        w = i
        m = selected - w
        num = ncr(men, m) * ncr(women, w)
        den = ncr(men + women, 5)
        p = num / den
        v = i * p
        print("No of women = ", w, " men ", m, " probability ", p, "  ", v)
        e = e + v

    print(e)


women_selection()

