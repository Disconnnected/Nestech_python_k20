number =600851475143

def isPrime (num):
    is_prime = True

    if num <= 1:
        is_prime = False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

    if is_prime:
        return True
    else:
        return False
listPrime=[]
# tìm các số nguyên tố từ 2-10000
for i in range(2,10000):
    if isPrime(i)==True:
        listPrime.append(i)
# tìm các số nguyên tố mà number chia cho là số không dư
for i in listPrime:
    if number%i==0:
        number=number/i
        print(f"{i} ",end='')
        
