"""Pattern 14: Print an increasing letter triangle starting with A.

Example for n = 5:
A
AB
ABC
ABCD
ABCDE
"""

def print_pattern(n):
    """Print an increasing letter triangle of height n."""
    for i in range(1, n + 1):
        row = [chr(65 + j) for j in range(i)]
        print(''.join(row))


if __name__ == '__main__':
    print_pattern(5)
