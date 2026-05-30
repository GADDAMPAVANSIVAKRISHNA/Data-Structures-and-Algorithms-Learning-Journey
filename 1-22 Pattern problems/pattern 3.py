"""Pattern 3: Print a left-aligned numeric triangle with each row showing 1..i.

Example for n = 5:
1
12
123
1234
12345
"""

def print_pattern(n):
    """Print a triangle where row i contains the numbers from 1 to i."""
    for i in range(1, n + 1):
        print(''.join(str(j) for j in range(1, i + 1)))


if __name__ == '__main__':
    print_pattern(5)
