"""
loại bỏ các phần tử rỗng trong chuỗi (trong trường hợp này là phần tử: "")

list_input = [1, 6, "Hương", "", ["vinamilk", "ông thọ"], "", 3.5]
"""

list_input = [1, 6, "Hương", "", ["vinamilk", "ông thọ"], "", 3.5]

for i in list_input:
    if i == "":
        list_input.remove(i)

print(list_input)