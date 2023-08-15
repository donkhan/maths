def p8():
    _l = [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7]
    s = ''
    for e in _l:
        if type(e) is str:
            if s == '':
                s = s + e
            else:
                s = s + '-' + e
    print(s)


def p9():
    li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
    nl = []
    for e in li:
        if e % 2 == 1:
            nl.append(e)
    print(nl)
    nl = []
    nl = [x for x in li if x % 2 == 1]
    print(nl)
    nl = []
    nl = list(filter(lambda x: (x % 2 == 1), li))
    print(nl)


def p10(l):
    return sum(l), len(l), min(l), sum(l)/len(l), max(l)


print(p10([1, 23, 3]))


def is_prime(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True

print(is_prime(13))


def factorial(n):
    p = 1
    for i in range(1, n+1):
        p = p * i
    return p

print(factorial(0))
print(factorial(8))


def p17():
    l = ['without','hello','bag','world']
    l.sort()
    print(l)

p17()


def q19(sentence):
    u = 0
    l = 0
    for c in sentence:
        if c >= 'A' and c <= 'Z':
            u = u + 1
        if c >= 'a' and c <= 'z':
            l = l + 1
    print("UPPER CASE ",u, " LOWER CASE ", l)

q19('aAB')


def q20(word):
    r = ''
    for i in range(len(word)-1, -1, -1):
        r = r + word[i]
    return r

print(q20('kavitha'))

def q16():
    x = "12,23,45"
    l = x.split(",")
    t = tuple(l)
    print(l)
    print(t)

q16()


def q8(_l):
    s = 0
    c = 0
    for e in _l:
        if type(e) is int or type(e) is float:
            s = s + e
        if type(s) is str:
            c = c + 1
    return s, c

print(q8([2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7] ))