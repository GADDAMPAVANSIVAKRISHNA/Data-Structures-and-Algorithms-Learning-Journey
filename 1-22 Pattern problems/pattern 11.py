"""Pattern 11: Print a binary number triangle alternating 0 and 1.

Example for n = 5:
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""

def print_pattern(n):
    """Print an alternating 0 and 1 triangle of height n."""
    for i in range(1, n + 1):
        start = 1 if i % 2 != 0 else 0
        row = [(start + j) % 2 for j in range(i)]
        print(' '.join(map(str, row)))


if __name__ == '__main__':
    print_pattern(5)
