"""Pattern 21: Print a hollow star square pattern with spaces.

Example for n = 4:
* * * *
*     *
*     *
* * * *
"""

def print_pattern(n):
    """Print a hollow star square pattern of size n."""
    for i in range(1, n + 1):
        if i == 1 or i == n:
            print(' '.join(['*'] * n))
        else:
            print('*' + ' ' * (2 * n - 3) + '*')


if __name__ == '__main__':
    print_pattern(4)
