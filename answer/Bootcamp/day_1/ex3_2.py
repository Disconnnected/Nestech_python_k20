#!/usr/bin/env python3
"""
Read:

- https://pymi.vn/tutorial/string1/
- https://www.familug.org/2015/07/go-strings-package-xu-ly-string.html
"""

data = """
Come to the
River
Of my
Soulful
Sentiments
Meandering silently
Yearning for release.
Hasten
Earnestly
As my love flows by
Rushing through the flood-gates
To your heart.
"""
# https://www.poetrysoup.com/poem/cross_my_heart_609765

import string

def solve(input_data):
    """Trả về tiêu đề bài thơ ghép từ các chữ cái đầu tiên của mỗi dòng.
    Chỉ viết hoa chữ cái đầu tiên.

    chú ý thay đổi trên input_data chứ không dùng trực tiếp data.
    """

    result = input_data.strip().splitlines()

    ## First way
    # first_letter = ""
    
    # for i in result:
    #     first_letter += i[0] + " "
    
    # result = first_letter

    # Second way
    result = " ".join(i[0] for i in result)

    return result


def main():
    """
    Cross my heart là một bài thơ thuộc thể loại "acrostic".
    Khi ghép các chữ cái HOẶC các từ đầu tiên lại với nhau thu được một
    thông điệp
    """
    print(solve(data))
    print("Result should be Pymi: {}".format(solve("P\nY\nM\nI")))


if __name__ == "__main__":
    main()
