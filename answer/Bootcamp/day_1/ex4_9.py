#!/usr/bin/env python3


def solve(numbers):
    """Tìm phần tử lớn nhất của list số nguyên `numbers`
    Không sử dụng function `max`, `sorted`

    Gợi ý: python có sẵn giá trị âm/dương vô cùng.
    """
    assert isinstance(numbers, list)
    result = None
    largest = float("-inf")

    for num in numbers:
        if num > largest:
            largest = num
    result = largest
    
    return result


def main():
    print(solve([-1, 5, 9, 6, -999999999999999, 1]))


if __name__ == "__main__":
    main()
