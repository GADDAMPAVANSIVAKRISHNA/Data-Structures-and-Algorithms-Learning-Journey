"""Pattern 19: Print a hollow symmetric star pattern.

Example for n = 5:
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
"""

def print_pattern(n):
    """Print a hollow symmetric star pattern of total height 2*n."""
    # Upper half
    for i in range(1, n + 1):
        stars = '*' * (n - i + 1)
        spaces = ' ' * (2 * (i - 1))
        print(stars + spaces + stars)
    # Lower half
    for i in range(1, n + 1):
        stars = '*' * i
        spaces = ' ' * (2 * (n - i))
        print(stars + spaces + stars)


if __name__ == '__main__':
    print_pattern(5)
