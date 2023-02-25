"""
loại bỏ các phần tử rỗng trong chuỗi (trong trường hợp này là phần tử: "")

list_input = [1, 6, "Hương", "", ["vinamilk", "ông thọ"], "", 3.5]
"""

list_input = [1, 6, "Hương", "", ["vinamilk", "ông thọ"], "", 3.5]

for i in list_input:
<<<<<<< HEAD:homework/day 2/ex7.py
    if i=='':
        list_input.remove(i)
=======
    if i == "":
        list_input.remove(i)

>>>>>>> ce1be8cee6e60a1d7368aec84d539cd6d1a7b484:homework/day 02/ex7.py
print(list_input)