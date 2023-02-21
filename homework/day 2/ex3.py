"""
Ghép nhiều chuỗi riêng biệt thành 1 chuỗi hoàn chỉnh, ngăn cách bởi dấu cách

đề bài:
    họ: "Nguyễn "
    Tên đệm: "Văn"
    Tên: "Tèo"

    output: Nguyễn Văn Tèo
"""

string1 = "Nguyễn"
string2 = "Văn"
string3 = "Tèo"

print(f"{string1} {string2} {string3}")
stringfullname = "{} {} {}".format(string1,string2,string3)
print(stringfullname)
