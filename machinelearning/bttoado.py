import numpy as np
import copy
# áp dụng công thức tính khoảng cách điểm A đến hình chiếu H trên đường thẳng:
# c^2 = h^2 + c'^2
# c'^ = ((c^2 - b^2 + a^2) / 2a)
def distance(triangleSide: list) -> float:
    a,b,c = triangleSide
    cc = ((c*c - b*b + a*a) / (2*a))
    h = np.sqrt(abs(c**2 - cc**2)) # giá trị máy tính có thể sai số -7.1e-15 (thực chất là 0) vì thế cần abs()
    return h

# Tính độ dài 3 cạnh của tam giác, (tọa độ O, điểm A, điểm tịnh tiến đồ thị)
# điểm tịnh tiến là điểm tự chọn, nó dùng để xác định a trong y = ax
# ví dụ: điểm có tọa độ (3,6) => y = 2x => a = 2
# bên dưới, ta sẽ đặt tên theo hình trên, cho dễ theo dõi, A điểm đã cho, B là góc tọa độ, C điểm tịnh tiến

def triangleSide(A : list, C: list) -> list:
    # điều kiện tọa độ x,y của C đều phải lớn hơn x,y của A
    
    # áp dụng định lý pytago để tính a, b, c theo hình
    Ax, Ay = A
    Cx, Cy = C
    
    a = np.sqrt(Cx**2 + Cy**2)
    b = np.sqrt((Cx-Ax)**2+(Cy-Ay)**2)
    c = np.sqrt(Ax**2+Ay**2)
    # print(f'{a} {b} {c}')
    return [a,b,c]

    
def coordinates(C: list, is_change_Cx: bool) -> list:
    Cx, Cy = C
    if is_change_Cx == True:
        C_new = [Cx + 1, Cy]
    else:
        C_new = [Cx,Cy + 1]
    # check tọa độ, tránh tính toán tọa độ trùng lần trước.
    # điều kiện, Cx or Cy khác 1, và Cx và Cy không chia hết cho nhau hoặc Cx và Cy đồng thời không chia hết cho 2
    Cx_new, Cy_new = C_new

    if Cx_new == 1 or Cy_new == 1:
        return C_new
    else:
        if (Cx_new % Cy_new == 0) or (Cy_new % Cx_new) == 0:
            return coordinates(C_new,is_change_Cx)
        elif (Cx_new % 2 == 0) and (Cy_new % 2 == 0):
            return coordinates(C_new,is_change_Cx)
        return C_new     

def straightLine(A_list, times : int  = 0,d_min : float = None, d_max: float = None, C : list = [2,1], C_min: list = None, is_change_Cx : bool = True):
    # times: số lần lặp lại để tịnh tiến tọa độ C (mỗi lần tịnh tiến 1 trục)
    # d_min: giá trị so sánh với kết quả tính, d_min tiệm cận về 0
    # Nếu d_sum > d_max: đổi trục tịnh tiến
    # C khác [0,0], vì tịnh tiến 1 lần 1 trục, nếu bằng 0, khoảng cách d không thay đổi
    print(times)
    # Tính d các điểm và d tổng
    d_list = [distance(triangleSide(A,C)) for A in A_list]
    d_sum = np.sum(d_list)
    print(f'''
C{C}
d_sum: {d_sum}
d_min: {d_min} d_max: {d_max}''')
    # so sánh kết quả
    ## 2 vòng đầu tiên để tìm d_min và d_max
    if d_min == None or d_max == None:
        if d_min == None:
            d_min = d_sum
            C_min = copy.copy(C)
        elif d_max == None:
            if d_sum <= d_min:
                d_max = d_min
                d_min = d_sum
            elif d_sum > d_min:
                d_max = d_sum
    ## các vòng sau sẽ update d_min or d_max
    else: 
        if d_sum <= d_min:
            d_min = d_sum
            C_min = copy.copy(C)
        elif d_sum > d_min:
            if d_sum >= d_max:
                is_change_Cx = not is_change_Cx
                print(f'-> is_change_Cx {"upCx" if is_change_Cx else "upCy"}')
            d_max = d_sum
            
    C_new = coordinates(C,is_change_Cx)
    print(f'C_new{C_new} (cho vòng lặp sau)')
    while times >= 1:
        times -= 1
        return straightLine(A_list, d_min=d_min,d_max=d_max,C=C_new,C_min=C_min,is_change_Cx=is_change_Cx, times=times)
    
    # Kết quả cuối cùng, tọa độ C_m, với a = C_my / C_mx
    print(f'''
    C_min{C_min}
    d_min = {d_min}
    a={C_min[1]/C_min[0]} 
          ''')
    return [C_min,d_min,C_min[1]/C_min[0]]
        

np.random.seed(0)
A_list = [[2,4],[3,7],[4,3],[35,23]]
A_list = np.random.randint(0,10,(4,2))
straightLine(A_list, times=993)

# tại sao chỉ có thể gọi lại tối đa 992 lần