# N-Queens
# Placing n queens on an n x n chessboard such that no two queens attack each other.


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
