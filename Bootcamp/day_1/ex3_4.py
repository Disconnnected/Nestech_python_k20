#!/usr/bin/env python3

"""
Viết chương trình loại bỏ phần mở rộng của một tên file bất kỳ.

Ví dụ::

  input_data = '....slsslslsls...sls'
  output = '....slsslslsls..'

  input_data = 'maria.data.mp9'
  output = 'maria.data'

Read: https://docs.python.org/3/library/stdtypes.html#str.rfind
"""


def solve(input_data):
    """Trả về tên file sau khi loại bỏ phần mở rộng

    :param input_data: tên file bất kì
    :rtype: str
    """
    result = None

    return result


def main():
    data = "maria.data.mp9"
    print(solve(data))


if __name__ == "__main__":
    main()


data = input("Please choose a file with format: ")
def data_1():
    for i in range(len(data)):
        if data[i] == "." :
            enddot = (data)[i:]
    return enddot
print(data_1())
print(data.removesuffix(data_1()))