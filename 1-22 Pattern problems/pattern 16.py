"""Pattern 16: Print a letter triangle with repeated characters.

Example for n = 5:
A
BB
CCC
DDDD
EEEEE
"""

def print_pattern(n):
    """Print a letter triangle with row-repeated characters of height n."""
    for i in range(1, n + 1):
        char = chr(65 + i - 1)
        print(char * i)


if __name__ == '__main__':
    print_pattern(5)
