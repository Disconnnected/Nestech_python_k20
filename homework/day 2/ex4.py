"""
nhận chuỗi vào là họ và tên, số tuổi của user (dùng hàm input)

in ra chuỗi: Họ và tên + số tuổi của user (với họ và tên viết in hoa)

ví dụ: "MAI PHƯƠNG THUÝ 39 TUỔI"
"""

ho_ten = input("Nhập họ và tên của bạn: ")
tuoi = input("Nhập số tuổi của bạn: ")
ho_ten = ho_ten.upper() # Chuyển họ tên sang chữ in hoa
print(ho_ten + " " + tuoi + " TUỔI")