def upper_diagonalize(m, v, index):
    if len(m) == index:
        return find_solution(m, v, 0, [0] * len(v))
    pivot = m[index][index]
    for i in range(index+1, len(m)):
        multiplier = m[i][index]
        for j in range(index, len(m[i])):
            m[i][j] = (m[i][j] * pivot) - (m[index][j] * multiplier)
        v[i] = (v[i] * pivot) - (v[index]*multiplier)
    return upper_diagonalize(m, v, index + 1)


def find_solution(m, v, index, s):
    if index == len(m):
        return s
    s = find_solution(m, v, index + 1, s)
    total = 0
    for i in range(index, len(v)):
        total = total + (m[index][i] * s[i])
    s[index] = (v[index] - total)/(m[index][index])
    return s


def solve():
    n = int(input("Enter the No of equations "))
    mat = []
    v = []
    for i in range(0, n):
        m = []
        mat.append(m)
        for j in range(0, n):
            m.append(float(input("mat[" + str(i) + "," + str(j) + "] = ")))
        v.append(float(input(" V[" + str(i) + "] = ")))
    s = upper_diagonalize(mat, v, 0)
    print("Solutions   ")
    for i in range(0, n):
        print(s[i])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print(upper_diagonalize([[1, 2, 1], [3, 4, 0], [5, 6, 2]], [4, 7, 13], 0))
    #print(upper_diagonalize([[2, 3], [3, -4]], [13, -6], 0))
    #print(upper_diagonalize([[2, 3, 4], [3, -4, 2], [-1, -2, 3]], [20, 1, 4], 0))
    solve()

