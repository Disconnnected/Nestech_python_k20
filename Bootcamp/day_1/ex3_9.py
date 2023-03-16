#!/usr/bin/env python3

"""
a, b, c là các số nguyên dương nhỏ hơn 10, biết a + b/c = 10

In ra list chứa các bộ số thỏa mãn điều kiện trên (a, b, c có thể trùng nhau).

Ví dụ:

- output: [[9, 1, 1], ...]
"""


def solve():
    """Trả về list chứa các list là các bộ số thỏa mãn đề bài

    Ví dụ:
        [[9, 1, 1], ..., [1, 9, 1]]

    Lưu ý: kết quả từng list con trả về với a giảm dần, b và c tăng dần
    """

    
    result = None


    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
lst = []
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            d = [a,b,c]
            if a + b/c == 10:
                lst.append(d)
                print(d)