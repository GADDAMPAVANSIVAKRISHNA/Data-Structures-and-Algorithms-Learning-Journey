"""Pattern 13: Print Floyd's Triangle.

Example for n = 5:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

def print_pattern(n):
    """Print Floyd's Triangle of height n."""
    num = 1
    for i in range(1, n + 1):
        row = []
        for _ in range(i):
            row.append(str(num))
            num += 1
        print(' '.join(row))


if __name__ == '__main__':
    print_pattern(5)
