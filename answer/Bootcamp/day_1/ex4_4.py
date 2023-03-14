#!/usr/bin/env python3

import time

def solve():
    """Tính số nghiệm của bài toán lớp 3

    Với các biến a,b,c,d,e,f,g,h,i là các số nằm trong khoảng 1-9 (các biến có
    thể có giá trị giống nhau), dạng biểu thức:

      a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 = 66

    rhs =  87 + f - a - d - (e*12)

    rhs2 = (rhs*i*c) - (13*b*i)

    (13*b/c) + (g*h/i) = 87 + f - a - d - (12*e)

	(13*b*i) + (g*h*c) = rhs*i*c

	(13*b*i) = c*((rhs*i) - (g*h))

    """ 
    """
    Bài toán áp dụng
    https://go.dev/play/p/euUskIcgtE
    https://viettuts.vn/bai-tap-python/phan-tich-so-nguyen-n-thanh-tich-cac-so-nguyen-to-trong-python
    https://gmaths.edu.vn/9-bai-toan-khien-cong-dong-mang-tren-toan-gioi-hai-nao-co-ca-mot-cau-danh-cho-hoc-sinh-lop-3-cua-viet-nam/
    https://stackoverflow.com/questions/42266204/solving-an-arithmetic-expression-with-multiple-answers-vietnamese-math-maze
    """
    start = time.time()

    result = 0

    ## Took 20~21 second
    for f in range(1,10):
        for a in range(1,10):
            for d in range(1,10):
                for e in range(1,10):
                    rhs =  87 + f - a - d - e * 12
                    if rhs != 0 and rhs > 0:
                        for c in range(1,10):
                            for i in range(1,10):
                                for b in range(1,10):
                                    rhs2 = rhs * i * c - 13 * b * i
                                    if (b * i) % c == 0 and rhs2 > 0:
                                        for h in range(1,10):
                                            for g in range(1,10):
                                                if h * g * c == rhs2:
                                                    result += 1                       
    

    ## Took 34~35 second
    # for b in range(1,10):
    #     for c in range(1,10):
    #         for d in range(1,10):
    #             for e in range(1,10):
    #                 for f in range(1,10):
    #                     for g in range(1,10):
    #                         for h in range(1,10):
    #                             for i in range(1,10):
    #                                 a = - 13 * b / c - d - 12 * e + f + 11 - g * h / i + 10 - 66
    #                                 if a > 0 and a < 10:
    #                                     result += 1

    print("Took: {} with new For loop".format(time.time() - start))
    
    return result



def main():
    print(solve())


if __name__ == "__main__":
    main()
