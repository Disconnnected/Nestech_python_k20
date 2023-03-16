#!/usr/bin/env python3


def solve(text):
    """Thực hiện biến đổi

      input: [a, abbbccccdddd, xxyyyxyyx]
      output: [a, abb3cc4dd4, xx2yy3xyy2x]

    Giải thích: Những chữ cái không lặp lại thì output giữ nguyên chữ cái đó.
    Những chữ cái liên tiếp sẽ in ra 2 lần + số lần lặp lại liên tiếp.

    Đây là một biến thể của một thuật toán nén dữ liệu có tên Run-length
    encoding (RLE).
    Không dùng groupby, hãy giải bài này.

    NOTE: bài này có thể giải dễ dàng dùng itertools.groupby
    https://pymotw.com/3/itertools/
    https://docs.python.org/3/howto/functional.html?highlight=iterator#functional-howto-iterators
    In [7]: for c, g in itertools.groupby('abbbccacdddd'):
    ...:     print("{}{}".format(c, len(list(g))), end="")
    ...:
    a1b3c2a1c1d4
    abbbccccdddd
    """
    result = None
    lst = []
    chars = ''
    text_new =''
    for index, char in enumerate(text):
        if(index > 0 and index < (len(text)-1)):
            if(char == text[index-1]):
                chars += char
            else:
                lst.append(chars)
                chars = char
        elif(index == (len(text)-1)):
            if(char == text[index-1]):
                chars += char
                lst.append(chars)
            else:
                lst.append(chars)
                lst.append(char)
        else:
            chars += char
    print(lst) 
    for i in lst:
        if(len(i)==1):
            text_new+=i
        else:
            text_new+=i[:2]+str(len(i))
    result = text_new
    return result


def main():
    print(solve("abbbccccddddeffg"))


if __name__ == "__main__":
    main()
