"""Pattern 22: Print a concentric number square pattern.

Example for n = 4:
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
"""

def print_pattern(n):
    """Print a concentric number square pattern of size 2*n - 1."""
    size = 2 * n - 1
    for r in range(size):
        row_vals = []
        for c in range(size):
            dist = min(r, c, size - 1 - r, size - 1 - c)
            row_vals.append(str(n - dist))
        print(' '.join(row_vals))


if __name__ == '__main__':
    print_pattern(4)
