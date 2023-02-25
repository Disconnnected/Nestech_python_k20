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
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
total=0
step=1
toantu=1
dau=1
for i in range(y):
    total= total+(toantu)*x**step
    step=step+2
    toantu=toantu*(-1)
    if(toantu==1):
        dau="+"
    elif(i==y-1):
        dau=""
    else:
        dau="-"
    print(f"({x})^{step}{dau}",end='')
print(f" ={total}")