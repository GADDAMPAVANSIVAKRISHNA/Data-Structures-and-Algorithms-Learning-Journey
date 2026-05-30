"""Pattern 7: Print a centered pyramid of odd asterisks.

Example for n = 5:
    *
   ***
  *****
 *******
*********
"""

def print_pattern(n):
    """Print a centered pyramid with 1, 3, 5, ... 2*n-1 stars."""
    for i in range(n):
        stars = '*' * (2 * i + 1)
        print(stars.center(2 * n - 1))


if __name__ == '__main__':
    print_pattern(5)
