#!/usr/bin/env python3

"""
Input: một số nguyên trong range(1,13,1). # start=1, stop=13, step=1
Output: tên tương ứng của tháng đó bằng tiếng Anh, và số ngày trong tháng đó.
Tháng 2 tính 28 ngày.

Ví dụ:

- input_data: 2

- output: February 28
"""
months = [["January", 31], 
          ["February", 28], 
          ["March", 31], 
          ["April", 30], 
          ["May", 31], 
          ["June", 30], 
          ["July", 31], 
          ["August", 31], 
          ["September", 30], 
          ["October", 31], 
          ["November", 30], 
          ["December", 31]]

def solve(input_data):
    """Trả về 1 `tuple` chứa 2 phần tử, ví dụ:

        input_data: 2
        output: ("February", 28)

    (1,2) là biểu diễn tương tự [1,2], chỉ thay dấu ngoặc vuông thành tròn.
    Đây là kiểu dữ liệu tuple.
    :param input_data: tháng bất kì
    :rtype: list
    """
    result = None
    for index,month_days in enumerate(months,start=1):
        if index==input_data:
            result= month_days
    return result


def main():
    month, day = solve(6)
    print(month, day)


if __name__ == "__main__":
    main()
