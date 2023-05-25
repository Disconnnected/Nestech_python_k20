"""
loại bỏ các phần tử rỗng trong chuỗi (trong trường hợp này là phần tử: "")

list_input = [1, 6, "Hương", "", ["vinamilk", "ông thọ"], "", 3.5]
"""
list_input = [1, 6, "Hương", "", ["vinamilk", "ông thọ"], "", 3.5]
list_output = []
i = 0
while (i < len(list_input)):
    if str(list_input[i]) is not "":
        list_output.append(list_input[i])
        i = i + 1
    else:
        list_input.pop(i)
print(list_output)

