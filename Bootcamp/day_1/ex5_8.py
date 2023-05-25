#!/usr/bin/env python3
import string

def solve():

    """Trả về biểu diễn của 20 mã ASCII từ 33 đến 53 theo format
    [(33, BIEUDIENCUA33), ...]
    Unicode codepoint của các số từ 0->9, a-z, A-Z.
    Unicode codepoint tương ứng với ký tự ``\t`` ``\n``, `` ``

    Gợi ý: dùng ``chr()``, ``ord()``.
    """
#     result = None

#     return result


# def main():
#     for part in solve():
#         print(part)
#         if isinstance(part, list):
#             for elem in part:
#                 print(elem)


# if __name__ == "__main__":
#     main()

ascii = [(i,chr(i)) for i in range(33,54)]
dig = [(i,chr(i)) for i in range(ord('0'), ord('9')+1)]
upper = [(i, chr(i)) for i in range(ord('A'), ord('Z')+1)]
lower = [(i, chr(i)) for i in range(ord('a'), ord('z')+1)]
tab = [ (ord('\t'),'\t'),
        (ord('\n'),'\n'),
        (ord(' '),' '),
        (ord('\r'),'r'),
        (ord('\b'),'b')]
print(ascii,'\n',
    dig,'\n',
    upper,'\n',
    lower,'\n',
    tab,'\n')





