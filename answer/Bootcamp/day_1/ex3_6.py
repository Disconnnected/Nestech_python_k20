#!/usr/bin/env python3

"""
Input: một số nguyên trong range(1,13,1). # start=1, stop=13, step=1
Output: tên tương ứng của tháng đó bằng tiếng Anh, và số ngày trong tháng đó.
Tháng 2 tính 28 ngày.

Ví dụ:

- input_data: 2

- output: February 28
"""

from calendar import *
import datetime

def solve(input_data):
    """Trả về 1 `tuple` chứa 2 phần tử, ví dụ:

        input_data: 2
        output: ("February", 28)

    (1,2) là biểu diễn tương tự [1,2], chỉ thay dấu ngoặc vuông thành tròn.
    Đây là kiểu dữ liệu tuple.
    :param input_data: tháng bất kì
    :rtype: list
    """
    result = input_data
    
    if result < 1:
        result = 1
    elif result > 12:
        result = 12
    
    # Lấy năm hiện tại
    today = datetime.date.today()
    year = today.year

    # Lấy số ngày trong tháng
    days_in_month = monthrange(year,result)[1]

    # Lấy tên của tháng nhập vào
    m_name = month_name[result]

    # Trả về dạng tuple
    result = tuple((m_name,days_in_month))
    
    return result


def main():
    ## Không hoạt động trên code
    # month, day = solve(0)
    # print(month, day)

    print(solve(1))

if __name__ == "__main__":
    main()
