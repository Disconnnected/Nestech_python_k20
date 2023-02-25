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