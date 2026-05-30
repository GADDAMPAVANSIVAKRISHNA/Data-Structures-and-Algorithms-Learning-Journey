"""Pattern 8: Print an inverted centered pyramid of odd asterisks.

Example for n = 5:
*********
 *******
  *****
   ***
    *
"""

def print_pattern(n):
    """Print an inverted centered pyramid with 2*n-1 down to 1 stars."""
    for i in range(n, 0, -1):
        stars = '*' * (2 * i - 1)
        print(stars.center(2 * n - 1))


if __name__ == '__main__':
    print_pattern(5)
