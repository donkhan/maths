

a = [
    [54, 95, 86, 128],
    [54, 96, 70, 75]
]

sum = 0
dull = 0
poor = 0
good_borderline = 0
bright_poor = 54

for i in range(0,  len(a)):
    for j in range(0, len(a[i])):
        if i == 1:
            poor = poor + a[i][j]
        if j == 2:
            dull = dull + a[i][j]
        if i == 0 and j == 3:
            good_borderline = good_borderline + a[i][j]
        sum = sum + a[i][j]

print(sum)

print(dull)
print(dull/sum)

print(poor)
print(poor/sum)

print(good_borderline)
print(good_borderline/sum)

print(bright_poor)
print(bright_poor/sum)

print(95)
print(95/sum)
