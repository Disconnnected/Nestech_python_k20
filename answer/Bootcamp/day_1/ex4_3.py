#!/usr/bin/env python3
import string

def solve(words):
    """Trả về list chứa điểm tương ứng của các từ trong `words`

    Nếu a b c d (không phân biệt chữ hoa thường) .... lần lượt bằng 1 2 3 4 ...
    thì từ ``attitude`` có giá trị bằng 100.

    Gợi ý::

      import string
      print(string.ascii_lowercase)
    """

    result = words
    lcharacter = string.ascii_lowercase
    sp = 0
    plist = []
    for i in words:
        for j in i:
            j = j.lower()
            for k in lcharacter:
                if j in k:
                    sp += lcharacter.index(j)+1
                    
        plist.append(sp)
        sp = 0
    
    print(words)

    result = plist

    return result


def main():
    words = [
        "attitude",
        "numpy",
        "django",
        "saltstack",
        "discipline",
        "Python",
        "FAMILUG",
        "pymi",
        "AAAaaa",
    ]

    print(solve(words))


if __name__ == "__main__":
    main()
