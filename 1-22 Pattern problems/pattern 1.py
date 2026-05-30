"""Pattern 1: Print a square of asterisks.

Example for n = 5:
*****
*****
*****
*****
*****
"""

def print_pattern(n):
    """Print an n x n square of asterisks."""
    for _ in range(n):
        print('*' * n)


if __name__ == '__main__':
    print_pattern(5)
