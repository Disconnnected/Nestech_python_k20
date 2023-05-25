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
data = ([2, 7, 11, 15], 9)


def solve(nums, target):
    """
    Trả về index của 2 số riêng biệt trong nums có tổng là target.

    Kiểm tra kết quả tại
    https://leetcode.com/problems/two-sum/
    """

    result = None


    return result


def main():
    nums, target = data
    print(solve(nums, target))


if __name__ == "__main__":
    main()



# nums = [1,2,3,4,5,0,6,7,8,9,10]
# nums.sort()
# target = int(input('Nhập target: '))
# for i in nums:
#     for j in nums:
#         if target == nums[i] + nums[j]:
#             print(f'{i,j}')

nums = data[0]
target = data[1]
for i in range(len(nums)):
    for j in range(len(nums)):
        if target == nums[i] + nums[j]:
            print(f'index (i,j): {i,j}')