"""
Ghép nhiều chuỗi riêng biệt thành 1 chuỗi hoàn chỉnh, ngăn cách bởi dấu cách

đề bài:
    họ: "Nguyễn "
    Tên đệm: "Văn"
    Tên: "Tèo"

    output: Nguyễn Văn Tèo
"""

input_list = ["Nguyễn", "Văn", "Tèo"]
new_line = ""

for i in input_list:
    new_line += i + " "

print(new_line)

