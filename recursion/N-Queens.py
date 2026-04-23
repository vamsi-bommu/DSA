# N-Queens
# Placing n queens on an n x n chessboard such that no two queens attack each other.


# Brute Force approach
def issafe(row, col, m, n):

    # Check left side
    for k in range(col):
        if m[row][k] == "Q":
            return False

    # Check upper-left diagonal
    r1 = row
    c1 = col
    while r1 >= 0 and c1 >= 0:
        if m[r1][c1] == "Q":
            return False

        r1 -= 1
        c1 -= 1

    # Check lower-left diagonal
    r2 = row
    c2 = col
    while c2 >= 0 and r2 < n:
        if m[r2][c2] == "Q":
            return False

        r2 += 1
        c2 -= 1

    return True


def n_queen(col, m, ans, n):
    if col >= n:
        ans.append([t[:] for t in m])
        return
    for j in range(n):
        if issafe(
            j, col, m, n
        ):  # checks each box to see if it is safe to place a queen
            m[j][col] = "Q"
            n_queen(col + 1, m, ans, n)
            m[j][col] = "."


ans = []
n = 4
n_queen(0, [["." for _ in range(n)] for _ in range(n)], ans, n)
print(ans)

# TC :
# SC :


# optimized approach


def n_queen(col, m, ans, n, rd, ud, ld):
    if col >= n:
        ans.append([t[:] for t in m])
        return
    for i in range(n):
        if rd[i] == 0 and ud[col + i] == 0 and ld[(n - 1) + (col - i)] == 0:
            m[i][col] = "Q"
            rd[i] = 1
            ud[col + i] = 1
            ld[(n - 1) + (col - i)] = 1
            n_queen(col + 1, m, ans, n, rd, ud, ld)
            m[i][col] = "."
            rd[i] = 0
            ud[col + i] = 0
            ld[(n - 1) + (col - i)] = 0


n = 4
ans = []
n_queen(
    0,
    [["." for i in range(n)] for j in range(n)],
    ans,
    n,
    [0 for i in range(n)],
    [0 for i in range(2 * n - 1)],
    [0 for i in range(2 * n - 1)],
)
print(ans)

# TC :
# SC :
