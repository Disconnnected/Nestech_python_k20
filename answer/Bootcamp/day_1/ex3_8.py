#!/usr/bin/env python3


def solve(input_data):
    """Kiểm tra input_data có phải là palindrome không.

    Một string được gọi là `palindrome` nếu viết xuôi hay ngược đều thu được
    kết quả như nhau (không phân biệt hoa thường, bỏ qua dấu space).
    String phải dài hơn 2 chữ cái.
    Ví dụ các palindrome: 'civic', 'Able was I ere I saw Elba', 'Noon'

    :rtype: bool
    """
    result = input_data.lower().split()

    char = result[0:][::-1]
    # print(char)
    rchar = [i[::-1] for i in result]
    # print(rchar)

    for i in range(len(result)):
        if char == rchar:
            result = True
        else:
            result = False
    return result


def main():
    print(solve("Able was I ere I saw Elba"))


if __name__ == "__main__":
    main()
