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
    result = ""

    for i,j in enumerate(text):
        if j != text[i-1]:
            if text.count(j)>1:
                result += "".join(f"{j}{j}{text.count(j)}")
            elif text.count(j)==1:
                result += "".join(f"{j}")
            else:
                result = "".join(f"{j}{text.count(j)}")
            
    return result


def main():
    print(solve("abbbccccdddd"))


if __name__ == "__main__":
    main()
