#!/usr/bin/env python3

"""
Xét các số nguyên dương < 100, in ra các số chia hết cho 5 theo dạng::

    5 == 1 * 5
    10 == 2 * 5
    15 == 3 * 5
    ...
"""


def solve():
    """Trả về 1 `list` các `string` có dạng:

        output: ['5 == 1 * 5', '10 == 2 * 5', ...]

    Lưu ý: Thứ tự tăng dần theo bảng cửu chương
    """
    result = None
    lst = []
    for num in range(1,100):
        if (num % 5 ==0):
           lst.append(f'{num} == {num/5:.0f} * 5')
    result=lst 

    return result


def main():
    for i in solve():
        print(i)


if __name__ == "__main__":
    main()
