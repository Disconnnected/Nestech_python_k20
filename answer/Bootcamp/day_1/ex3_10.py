#!/usr/bin/env python3

"""
Làm thêm tùy chọn:
- https://projecteuler.net/problem=1
- https://projecteuler.net/problem=2
- https://projecteuler.net/problem=3
- https://projecteuler.net/problem=4
- https://projecteuler.net/problem=5
- https://projecteuler.net/problem=6
- https://projecteuler.net/problem=7
- https://projecteuler.net/problem=8
- https://projecteuler.net/problem=9
- https://projecteuler.net/problem=10
- https://projecteuler.net/problem=16
"""
data = ([2, 7, 11,15], 9)


def solve(nums, target):
    """
    Trả về index của 2 số riêng biệt trong nums có tổng là target.

    Kiểm tra kết quả tại
    https://leetcode.com/problems/two-sum/
    """

    result = None
    for index1, num1 in enumerate(data[0]):
        if(result == None):
            for index2, num2 in enumerate(data[0]):
                if((index1 < index2) & (num1+num2 ==data[1])):
                    result=[index1,index2]
                    break
        else:
            break   
    return result


def main():
    nums, target = data
    print(solve(nums, target))


if __name__ == "__main__":
    main()
