"""Pattern 4: Print a left-aligned triangle where row i repeats digit i.

Example for n = 5:
1
22
333
4444
55555
"""

def print_pattern(n):
    """Print a triangle where the i-th row contains the digit i repeated i times."""
    for i in range(1, n + 1):
        print(str(i) * i)


if __name__ == '__main__':
    print_pattern(5)
