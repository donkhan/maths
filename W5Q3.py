def rest(l):
    if length(l) == 0:
        return l
    return l[1:]


def first(l):
    return l[0]


def length(l):
    if l is None:
        return 0
    return len(l)


def sl(X):
    outlist = []
    newList = X
    while (length(newList) > 0):
        outlist.append(first(newList))
        newList = rest(rest(newList))
    return (outlist)

N = [1,2,3,4,5,6,7,8,9,10]
N = [1,2,2,3,3]

A = sl(N)
B = sl(rest(N))
print(A)
print(B)

count = 0
for y in A:
    for z in B:
        if y == z:
            count = count + 1

print(count)

