"""Pattern 15: Print a decreasing letter triangle starting with A.

Example for n = 5:
ABCDE
ABCD
ABC
AB
A
"""

def print_pattern(n):
    """Print a decreasing letter triangle of initial width n."""
    for i in range(n, 0, -1):
        row = [chr(65 + j) for j in range(i)]
        print(''.join(row))


if __name__ == '__main__':
    print_pattern(5)
