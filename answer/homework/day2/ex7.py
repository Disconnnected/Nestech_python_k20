"""
loại bỏ các phần tử rỗng trong chuỗi (trong trường hợp này là phần tử: "")

list_input = [1, 6, "Hương", "", ["vinamilk", "ông thọ"], "", 3.5]
"""

list_input = [1, 6, "Hương", "",["vinamilk", "ông thọ"], "", 3.5]

list_output = []

for ele in list_input:
    if ele != "":
        list_output.append(ele)
print('cach 1: ',list_output)

# cách khác

while "" in list_input:
    list_input.remove("")

print('cach 2: ',list_input)
