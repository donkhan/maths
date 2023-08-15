

def sieve(upper):
    r = list()
    l = list()
    for i in range(2, upper+1):
        l.append({'key': 'N', 'no': i})

    for i in range(0, len(l)):
        e = l[i]
        if e['key'] == 'Y':
            continue

        for j in range(i+1, len(l)):
            x = l[j]
            if x['no'] % e['no'] == 0:
                x['key'] = 'Y'

    for e in l:
        if e['key'] == 'N':
            r.append(e['no'])
    return r


l = sieve(1000)
n1 = 296
n2 = 481

for e in l:
    if n1 % e == 0 and n2 %e == 0:
        print(e)
print(l)


