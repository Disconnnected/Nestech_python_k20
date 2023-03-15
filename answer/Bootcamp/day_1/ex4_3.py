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

    result = None
    letters = string.ascii_lowercase
    value_words = []
    for word in words:
        value = 0
        for el in word:
            value += (letters.index(el.lower())+1)
        value_words.append(value)
    
    result = value_words
    return result


def main():
    words = [
        "numpy",
        "django",
        "saltstack",
        "discipline",
        "Python",
        "FAMILUG",
        "pymi",
    ]
    
    
    print(solve(words))


if __name__ == "__main__":
    main()
