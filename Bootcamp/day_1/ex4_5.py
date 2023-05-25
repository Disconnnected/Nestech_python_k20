#!/usr/bin/env python3


def solve(numbers):
    """Tính tổng và tích của dãy số `numbers`

    Return một tuple (sum, product)
    Không sử dụng hàm `sum`
    """

#     result = None


#     return result


# def main():
#     # Cho list numbers chứa các số chẵn từ -10 đến 10, trừ số 0.
#     numbers = range(-10, 11, 2)  # step=2
#     numbers = list(numbers)
#     numbers.remove(0)

#     result = solve(numbers)
#     print(result)
#     assert result == (0, -14745600)


# if __name__ == "__main__":
#     main()


numbers = range(-10, 11, 2)  # step=2
numbers = list(numbers)
numbers.remove(0)
sum = 0
product = 1
for i in numbers:
    sum += i
    product *= i
print(f"Tổng tự tính {sum}")
print(f'Tích tự tính {product}')