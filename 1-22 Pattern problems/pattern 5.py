"""Pattern 5: Print an inverted left-aligned triangle of asterisks.

Example for n = 5:
*****
****
***
**
*
"""

def print_pattern(n):
    """Print an inverted left-aligned triangle of asterisks."""
    for i in range(n, 0, -1):
        print('*' * i)


if __name__ == '__main__':
    print_pattern(5)
