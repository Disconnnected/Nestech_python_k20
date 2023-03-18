#!/usr/bin/env python3
import numpy as np
from math import factorial
"""
[Không bắt buộc]

Bắt đầu từ góc trên bên trái của ô có kích thước 2x2, và chỉ cho phép di chuyển
sang phải hoặc xuống dưới, có chính xác 6 đường để đi đến góc dưới bên phải.

Có bao nhiêu đường như vậy trong ô 10x10?

Kiểm tra kết quả bằng https://projecteuler.net/problem=15
"""


def solve():
    # Viết code vào đây set result làm kết quả của tính toán
    #
    #
    #Tính mỗi lần di chuyển bằng cách tính giai thừa đến số ô 
    
    f = factorial(20)/(factorial(10)*factorial(20-10))

    result = f"Số hướng đường đi trong ô 10x10: {str(f)} bước"
      

    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
