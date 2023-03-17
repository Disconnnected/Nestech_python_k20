#!/usr/bin/env python3
import string

def solve():

    """Trả về biểu diễn của 20 mã ASCII từ 33 đến 53 theo format
    [(33, BIEUDIENCUA33), ...]
    Unicode codepoint của các số từ 0->9, a-z, A-Z.
    Unicode codepoint tương ứng với ký tự ``\t`` ``\n``, `` ``

    Gợi ý: dùng ``chr()``, ``ord()``.
    """
    result = None
    ascii_list = [(i, chr(i)) for i in range(33,54)]
    unicode_digits = [(i,chr(i)) for i in range(ord('0'),ord('9')+1)]
    unicode_uppercase = [(i,chr(i)) for i in range(ord('A'),ord('Z')+1)]
    unicode_lowercase = [(i,chr(i)) for i in range(ord('a'),ord('z')+1)]
    unicode_tnb = [(ord('\t'),'\t'),
                   (ord('\n'),'\n'),
                   (ord(' '),' ')]
    
    print(unicode_tnb)
    result=[ascii_list,
            unicode_digits,
            unicode_uppercase,
            unicode_lowercase,
            unicode_tnb
            ]
    return result


def main():
    for part in solve():
        print(part)
        # if isinstance(part, list):
        #     for elem in part:
        #         print(elem)


if __name__ == "__main__":
    main()
