"""Pattern 6: Print a decreasing numeric triangle.

Example for n = 5:
12345
1234
123
12
1
"""

def print_pattern(n):
    """Print rows of numbers from 1 to decreasing row length."""
    for i in range(n, 0, -1):
        print(''.join(str(j) for j in range(1, i + 1)))


if __name__ == '__main__':
    print_pattern(5)
