#!/usr/bin/env python3


def solve(input_data):
    """
    Trả về string biễu diễn tương ứng ở hệ thập phân (decimal),
    hệ nhị phân (binary), bát phân (octal), thập lục phân (heximal)

    Gợi ý: sử dụng bin(), oct(), hex(), string method `rjust`
    Mỗi dòng 1 số, với độ rộng là 8, các giá trị thẳng nhau căn lề phải.
    Output :

       1       1     0o1     0x1
       2      10     0o2     0x2
       ...
    """
    result = None
    rows =''
    for i in input_data:
        rows += f"{i:>8}{bin(i):>8}{oct(i):>8}{hex(i):>8}\n"
    result = rows
    return result


def main():
    input_data = range(1, 20)
    print(solve(input_data))


if __name__ == "__main__":
    main()
