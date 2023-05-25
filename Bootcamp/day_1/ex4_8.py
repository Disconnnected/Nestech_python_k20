#!/usr/bin/env python3


def solve():
    """Trả về list N bộ integer (a, b, c) là độ dài 3 cạnh của tam giác vuông
    cạnh huyền `c` có chu vi 24 cm (perimeter), biết độ dài các cạnh <= 10cm.

    Yêu cầu dùng list comprehension.
    """
    result = None


    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()

a = {a for a in range(1,11)}
b = {b for b in range(1,11)}
c = {c for c in range(1,11)}
# p = a + b + c
for a in a:
    for b in b:
        for c in c:
            if a + b + c == 24:
                print(a + b + c )

