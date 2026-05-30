"""Pattern 9: Print a diamond of odd asterisks.

Example for n = 5:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""

def print_pattern(n):
    """Print a centered diamond with odd star counts up to 2*n-1."""
    width = 2 * n - 1
    for i in range(1, n + 1):
        stars = '*' * (2 * i - 1)
        print(stars.center(width))
    for i in range(n - 1, 0, -1):
        stars = '*' * (2 * i - 1)
        print(stars.center(width))


if __name__ == '__main__':
    print_pattern(5)
