"""
Ghép nhiều chuỗi riêng biệt thành 1 chuỗi hoàn chỉnh, ngăn cách bởi dấu cách

đề bài:
    họ: "Nguyễn "
    Tên đệm: "Văn"
    Tên: "Tèo"

    output: Nguyễn Văn Tèo
"""

first_name = 'Nguyễn '
middle_name = 'Văn'
last_name = 'Tèo'

full_name = first_name.strip() + ' '+middle_name.strip()+' '+last_name.strip()
print(full_name)

# cách khác
name_lst = ['Nguyễn ','Văn','Tèo']
full_name2 = ''
for name in name_lst:
    full_name2 += name.strip()+' '
full_name2=full_name2.strip()
print(full_name2)

# cách khác
first_name = 'Nguyễn '
middle_name = 'Văn'
last_name = 'Tèo'

full_name3 = f'{first_name}{middle_name} {last_name}'
print(full_name3)

