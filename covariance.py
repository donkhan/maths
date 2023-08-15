x = [4, 5, 1, 2, 3, 5, 4]
y = [15, 10, 17, 12, 16, 10, 13]

#x = [1, 2, 3, 4, 5]
#y = [75, 85, 94, 101, 108]

x_ = sum(x)/len(x)
y_ = sum(y)/len(y)

print(x_)
print(y_)

#xmx = [e-x_ for e in x]
#print(xmx)

xm = []
for e in x:
    xm.append(e - x_)

ym = []
for e in y:
    ym.append(e - y_)

print(xm)
print(ym)

t = []
s = 0
for i in range(0, len(x)):
    t_ = (xm[i] * ym[i])
    t.append(t_)
    s = s + t_

print(t)
print(s)

print(s/len(x))
print(s/6)

