#!/usr/bin/env python3
import string

def solve():

    """Trả về biểu diễn của 20 mã ASCII từ 33 đến 53 theo format
    [(33, BIEUDIENCUA33), ...]
    Unicode codepoint của các số từ 0->9, a-z, A-Z.
    Unicode codepoint tương ứng với ký tự ``\t`` ``\n``, `` ``

    Gợi ý: dùng ``chr()``, ``ord()``.
    """ 

    result = []
    
    for a in range(33,54):
        result += [(a,chr(a))]

    for d in range(ord("0"),ord("9")+1):
        result += [(d,chr(d))]

    for l in range(ord("a"),ord("z")+1):
        result += [(l,chr(l))]
    
    for u in range(ord("A"),ord("Z")+1):
        result += [(u,chr(u))]

    result += [(ord('\t'),'\t'), (ord('\n'),'\n'), (ord(' '),' ')]
    
    return result


def main():
    for part in solve():
        print(part)
        if isinstance(part, list):
            for elem in part:
                print(elem)


if __name__ == "__main__":
    main()
