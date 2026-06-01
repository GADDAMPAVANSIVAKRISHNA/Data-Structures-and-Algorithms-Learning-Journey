"""Pattern 20: Print a symmetric butterfly star pattern.

Example for n = 5:
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
"""

def print_pattern(n):
    """Print a symmetric butterfly star pattern of total height 2*n - 1."""
    # Top half (including middle row)
    for i in range(1, n + 1):
        stars = '*' * i
        spaces = ' ' * (2 * (n - i))
        print(stars + spaces + stars)
    # Bottom half
    for i in range(n - 1, 0, -1):
        stars = '*' * i
        spaces = ' ' * (2 * (n - i))
        print(stars + spaces + stars)


if __name__ == '__main__':
    print_pattern(5)
