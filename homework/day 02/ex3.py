"""
Ghép nhiều chuỗi riêng biệt thành 1 chuỗi hoàn chỉnh, ngăn cách bởi dấu cách

đề bài:
    họ: "Nguyễn "
    Tên đệm: "Văn"
    Tên: "Tèo"

    output: Nguyễn Văn Tèo
"""

<<<<<<< HEAD:homework/day 2/ex3.py
string1 = "Nguyễn"
string2 = "Văn"
string3 = "Tèo"

print(f"{string1} {string2} {string3}")
stringfullname = "{} {} {}".format(string1,string2,string3)
print(stringfullname)
=======
input_list = ["Nguyễn", "Văn", "Tèo"]
new_line = ""

for i in input_list:
    new_line += i + " "

print(new_line)

>>>>>>> ce1be8cee6e60a1d7368aec84d539cd6d1a7b484:homework/day 02/ex3.py
