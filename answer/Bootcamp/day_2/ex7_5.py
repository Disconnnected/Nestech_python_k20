#!/usr/bin/env python3

import inspect
import os
import sys

def solve(*args, **kwargs):
    """Return tuple chứa
    - Đường dẫn tới code của module `os`
    - list chứa các attribute của os và sys
    - Số dòng trong module `os`

    Biết dir(object) sẽ trả về tất cả thuộc tính (attribute) của object đó.
    Module cũng là object.
    
    In [11]: import os

    In [12]: len(dir(os))
    Out[12]: 284
    """

    result = None
    # Đường dẫn tới code của module `os`
    os_path = os.__file__
    # print(os_path)
    
    # list chứa các attribute của os và sys
    list_atrri = dir(os) + dir(sys)
    # print(list_atrri)
    
    # Số dòng trong module `os`
    lines_os = 0
    with open(os_path) as f:
        for line in f:
            lines_os += 1
    print(lines_os)
    
    print(len(inspect.getsourcelines(os)[0]))

    result = (os_path, list_atrri ,lines_os)
    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
