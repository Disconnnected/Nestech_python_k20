#!/usr/bin/env python3
# data = 1000


# def solve(input_data):
#     """Đầu vào: một số nguyên dương

#     Đầu ra: số nguyên tạo bởi phần từ số 1 cuối cùng trở về bên
#     phải - của dạng binary của số đầu vào.

#     Ví dụ::

#       input_data = 5 # (0b101)
#       output = 1

#       input_data = 24 (11000)
#       output = 1000

#       input_data = 9 (1001)
#       output = 1

#     Hàm có sẵn: bin(10) == '0b1010'
#     Hàm có sẵn tạo ra integer từ string: 69 == int('69')
#     """
#     result = None

#     # code here

#     return result

# def main():
#     print(solve(data))

# if __name__ == "__main__":
#     main()

# def bin_1(data):
#     reverse = bin(data)
#     # reverse = reverse[::-1]
#     return reverse
# user = int(input('nhập 1 số: '))

# print(bin_1(user))



data = 24
print(bin(data))
print(bin(data)[3:])

print(bin(data).split('0',1))

