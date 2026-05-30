"""Pattern 10: Print a left-aligned triangle that grows then shrinks.

Example for n = 5:
*
**
***
****
*****
****
***
**
"""

def print_pattern(n):
    """Print a left-aligned pattern that increases to n then decreases."""
    for i in range(1, n + 1):
        print('*' * i)
    for i in range(n - 1, 0, -1):
        print('*' * i)


if __name__ == '__main__':
    print_pattern(5)
