"""Pattern 18: Print a letter triangle starting from the back.

Example for n = 5:
E
D E
C D E
B C D E
A B C D E
"""

def print_pattern(n):
    """Print a letter triangle ending at n-th letter of height n."""
    for i in range(1, n + 1):
        row = [chr(65 + n - i + j) for j in range(i)]
        print(' '.join(row))


if __name__ == '__main__':
    print_pattern(5)
