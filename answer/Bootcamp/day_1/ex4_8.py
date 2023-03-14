#!/usr/bin/env python3


def solve():
    """Trả về list N bộ integer (a, b, c) là độ dài 3 cạnh của tam giác vuông
    cạnh huyền `c` có chu vi 24 cm (perimeter), biết độ dài các cạnh <= 10cm.

    Yêu cầu dùng list comprehension.
    """
    result = [(a,b,24) for a in range(1,11) for b in range(1,11) if a <= 10 and a == b and 24%b == 0]

    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
