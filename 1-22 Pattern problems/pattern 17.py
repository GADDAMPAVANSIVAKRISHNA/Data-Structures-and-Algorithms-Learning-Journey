"""Pattern 17: Print a centered letter pyramid.

Example for n = 4:
   A
  ABA
 ABCBA
ABCDCBA
"""

def print_pattern(n):
    """Print a centered letter pyramid of height n."""
    for i in range(1, n + 1):
        # Spaces: n - i
        spaces = " " * (n - i)
        # Characters: ascending 0 to i-1, then descending i-2 down to 0
        chars = []
        for j in range(i):
            chars.append(chr(65 + j))
        for j in range(i - 2, -1, -1):
            chars.append(chr(65 + j))
        print(spaces + "".join(chars))


if __name__ == '__main__':
    print_pattern(4)
