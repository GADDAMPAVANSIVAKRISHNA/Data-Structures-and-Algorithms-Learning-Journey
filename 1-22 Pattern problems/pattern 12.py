"""Pattern 12: Print a number crown pattern.

Example for n = 4:
1      1
12    21
123  321
12344321
"""

def print_pattern(n):
    """Print a number crown of height n."""
    for i in range(1, n + 1):
        # Left part: 1 to i
        left = "".join(str(x) for x in range(1, i + 1))
        # Spaces: 2 * (n - i)
        spaces = " " * (2 * (n - i))
        # Right part: i down to 1
        right = "".join(str(x) for x in range(i, 0, -1))
        print(left + spaces + right)


if __name__ == '__main__':
    print_pattern(4)
