#!/usr/bin/env python3
import string

def solve(words):
    """Trả về list chứa điểm tương ứng của các từ trong `words`

    Nếu a b c d (không phân biệt chữ hoa thường) .... lần lượt bằng 1 2 3 4 ...
    a có giá trị là 1
    t có giát trại là bao nhiêu đấy
    i có giá trị là 9
    thì từ ``attitude`` có giá trị bằng 100.

    Gợi ý::

      import string
      print(string.ascii_lowercase)
    """

    result = None
    # sample = "attitude"
    # import string
    # lower = string.ascii_lowercase
    # for i in lower:
    #     print(sample.find(i) + 1)
        




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


sample = "attitude"
words = [
        "numpy",
        "django",
        "saltstack",
        "discipline",
        "Python",
        "FAMILUG",
        "pymi",
    ]
lower = string.ascii_lowercase
for w in words: # lấy từng từ
    v = 0 # tạo biến
    for i in w: #xét từng chữ 
        v += lower.index(i.lower())+1   
    print(f'{w}: {v}')