#!/usr/bin/env python3

"""
Input: một số nguyên trong range(1,13,1). # start=1, stop=13, step=1
Output: tên tương ứng của tháng đó bằng tiếng Anh, và số ngày trong tháng đó.
Tháng 2 tính 28 ngày.

Ví dụ:

- input_data: 2

- output: February 28
"""


def solve(input_data):
    """Trả về 1 `tuple` chứa 2 phần tử, ví dụ:

        input_data: 2
        output: ("February", 28)

    (1,2) là biểu diễn tương tự [1,2], chỉ thay dấu ngoặc vuông thành tròn.
    Đây là kiểu dữ liệu tuple.
    :param input_data: tháng bất kì
    :rtype: list
    """
#     result = None

#     return result


# def main():
#     month, day = solve(0)
#     print(month, day)


# if __name__ == "__main__":
#     main()
while True:
    input_data = input('Nhập tháng: ')
    for i in range(1, 13, 1):
        month = int(input_data)
        if i == month:
            if i % 2 == 1 and i < 8 or i % 2 == 0 and i > 7:
                date = str(31)
            if i == 2:
                date = str(28)
            elif i % 2 == 0 and i < 8 or i % 2 == 1 and i > 7:
                date = str(30)
            print(f'Tháng {i} có: {date} ngày')
            print(f'({input_data.strip()}, {date.strip()})')


