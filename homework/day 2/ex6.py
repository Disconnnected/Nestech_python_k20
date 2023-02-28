"""

cho chuỗi: list_input = [1,2,3,4,5,6,7,8]

in ra chuỗi mới với mỗi phần tử của chuỗi mới là bình thương của phần tử tương ứng trong chuỗi cũ

expected_output = [1,4,9,16,25,36,49,64]

"""
num = int(input("Nhập một số nguyên dương: "))

is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "là số nguyên tố")
else:
    print(num, "không là số nguyên tố")