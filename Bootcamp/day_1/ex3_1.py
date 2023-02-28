#!/usr/bin/env python3
data = 24

def last_one(n):
    binary =  bin(n)[2:]  # Chuyển đổi sang dạng binary và bỏ đi ký tự '0b' ở đầu
    last_one_index = binary.rfind('1')  # Tìm vị trí của phần tử số 1 cuối cùng trong dạng binary
    print(binary)
    print(last_one_index)
    return int(binary[last_one_index:]) if last_one_index != -1 else 0  # Tạo số nguyên từ phần từ số 1 cuối cùng và trả về

def solve(input_data):
    """Đầu vào: một số nguyên dương

    Đầu ra: số nguyên tạo bởi phần từ số 1 cuối cùng trở về bên
    phải - của dạng binary của số đầu vào.
    binary = bin(n)[2:]
    
    Ví dụ::

      input_data = 5 # (0b101)
      output = 1

      input_data = 24 (11000)
      output = 1000

      input_data = 9 (1001)
      output = 1

    Hàm có sẵn: bin(10) == '0b1010'
    Hàm có sẵn tạo ra integer từ string: 69 == int('69')
    """

    result = last_one(input_data)

    # code here

    return result



def main():
    print(last_one(data))

if __name__ == "__main__":
    main()
