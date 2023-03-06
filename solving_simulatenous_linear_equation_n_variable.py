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


def solve_t1():
    m = [
            [1, 2, 1],
            [3, 4, 0],
            [5, 6, 2]
        ]
    v = [4, 7, 13]
    s = upper_diagonalize(m, v, 0)
    print(s)


def solve_t2():
    m = [[2, 3], [3, -4]]
    v = [13, -6]
    s = upper_diagonalize(m, v, 0)
    print(s)


def solve_t3():
    m = [[2, 3, 4], [3, -4, 2], [-1, -2, 3]]
    v = [20, 1, 4]
    s = upper_diagonalize(m, v, 0)
    print(s)


def solve():
    n = int(input("Enter the No of equations "))
    mat = []
    v = []
    for i in range(0, n):
        m = []
        mat.append(m)
        for j in range(0, n):
            m.append(int(input("mat[" + str(i) + "," + str(j) + "] = ")))
        v.append(int(input(" V[" + str(i) + "] = ")))
    s = upper_diagonalize(mat, v, 0)
    print("Solutions   ")
    for i in range(0, n):
        print(s[i])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #solve_t2()
    #solve_t3()
    #solve_t1()
    solve()

