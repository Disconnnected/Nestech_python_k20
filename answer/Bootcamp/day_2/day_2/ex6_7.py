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
    result = ""

    for i in input_data:
        n = str(i).rjust(8)
        b = str(bin(i)[bin(i).rfind('1'):]).rjust(8)
        o = str(oct(i)).rjust(8)
        h = str(hex(i)).rjust(8)

        result += n + b + o + h + "\n"
    
    return result


def main():
    input_data = range(1, 20)
    print(solve(input_data))


if __name__ == "__main__":
    main()