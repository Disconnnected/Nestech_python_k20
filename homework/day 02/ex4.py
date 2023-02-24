"""
nhận chuỗi vào là họ và tên, số tuổi của user (dùng hàm input)

in ra chuỗi: Họ và tên + số tuổi của user (với họ và tên viết in hoa)

ví dụ: "MAI PHƯƠNG THUÝ 39 TUỔI"
"""

fullname = input("Họ và tên của user: \n")
age = input("Tuổi của user: \n")

print(f"{fullname} {age} tuổi".upper())
