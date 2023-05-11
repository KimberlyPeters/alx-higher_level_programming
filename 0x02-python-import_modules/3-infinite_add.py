#!/usr/bin/python3

if __name__ == "__main__":
    """Print the result of adding all arguments."""
    import sys

    arguments = sys.argv[1:]
    total = 0

    for arg in arguments:
        total += int(arg)

    print(total)
