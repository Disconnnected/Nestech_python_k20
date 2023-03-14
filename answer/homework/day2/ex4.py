"""
nhận chuỗi vào là họ và tên, số tuổi của user (dùng hàm input)

in ra chuỗi: Họ và tên + số tuổi của user (với họ và tên viết in hoa)

ví dụ: "MAI PHƯƠNG THUÝ 39 TUỔI"
"""

full_name = input('Nhập họ tên của bạn: ')
age = int(input('Nhập tuổi của bạn: '))

print(f'{full_name.upper()} {age} TUỐI')

#  cách khác
result = '{} {} tuổi'.format(full_name, age)
print(result.upper())