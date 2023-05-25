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



def bin_one(data):
    for i in range(len(bin(data))): 
        if bin(data)[i] == "1" : #nếu bin data tại vị trí thứ i = 1
            bin_data = (bin(data)[i:]) #thì lấy bin từ chỗ này về sau
    return "the binary from the last number 1: " + bin_data 
while True:
    try:
        ask_user = input('''Please choose number or exit: ''')
        if ask_user == ("exit"):
            exit()
        else:
            data = int(ask_user)
            print(bin_one(data))
    except ValueError:
        False
