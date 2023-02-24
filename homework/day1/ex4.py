number = int(input("nhập số muốn ghi: "))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for  i in range(1,int(number/2)):
    if(is_prime(i)==True and is_prime(number - i)==True):
        print(f"{number} có thể viết như sau: {i}+{number-i}")

