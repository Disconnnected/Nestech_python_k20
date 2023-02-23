# function
# variable = value

# def sum(a, b):
#     return a+b

# tổng = sum(100, 150)
# print(tổng)

"""
mỗi ngày, Vinh đi làm mất 8k gửi xe, 15k ăn sáng, 30k ăn trưa
tính tổng mỗi tháng Vinh mất bao nhiêu tiền cho các chi phí trên, cho biết 1 tháng có 30 ngày, và ngày nào Vinh cx ăn uống như vậy
    sử dụng function
"""

def fee(parking_fee = 8000, breakfast = 15000, lunch = 30000):
# def fee(parking_fee, breakfast, lunch):
    print("parking_fee")
    print("breakfast")
    print("lunch")
    total_fee_per_day = parking_fee +  breakfast + lunch
    total_fee_per_month = total_fee_per_day * 30
    return f"Tổng chi phí của Vinh là: {total_fee_per_month}"
#     return [parking_fee, breakfast, lunch]
# #
#     return total_fee_per_month
