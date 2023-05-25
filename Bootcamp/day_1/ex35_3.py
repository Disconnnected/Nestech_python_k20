#!/usr/bin/env python3


def solve(N):
    """Creates a list which contains N first even integers. ``[2, 4 ...]``
    Must: use list comprehension
    Tips: list comprehension always create new list
    """
    result = [x*2 for x in range(N)]

    return result


def main():
    print(solve(6))


if __name__ == "__main__":
    main()
