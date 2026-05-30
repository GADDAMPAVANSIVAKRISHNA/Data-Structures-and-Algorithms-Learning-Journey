"""Pattern 2: Print a left-aligned increasing triangle of asterisks.

Example for n = 5:
*
**
***
****
*****
"""

def print_pattern(n):
    """Print a left-aligned triangle with rows 1..n of asterisks."""
    for i in range(1, n + 1):
        print('*' * i)


if __name__ == '__main__':
    print_pattern(5)
