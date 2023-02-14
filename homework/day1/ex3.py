"""
cho dãy số từ 1 đến 100
in ra các số thoả mãn điều kiện:
    - chia hết cho 2
    - chia hết cho 3
    (chia hết cho cả 2 và 3)
    

Hướng dẫn làm bài: 
    - xoá dấu "..." và điền kết quả thích hợp

Giải thích code:
    - range(1,100) ==> lấy danh sách các số từ 1 đến 100
    - "% 2 == 0" ==> dấu % biểu thị cho phép chia lấy dư. ví dụ: 11 chia 2 bằng 5, dư 1. như vậy 11 % 2 == 1
    - "and": kết hợp cả 2 điều kiện. trong trường hợp này là kết hợp cả điều kiện chia hết cho 2 và điều kiện chia hết cho 3
"""

#làm tiếp tại đây, nhấn control + F5 để chạy

for i in range(1,100):
    if ... % 2 == 0 and ... % ... == 0: 
        print(...)