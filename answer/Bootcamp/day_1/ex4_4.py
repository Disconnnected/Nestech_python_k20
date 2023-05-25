#!/usr/bin/env python3

import time

def solve():
    """Tính số nghiệm của bài toán lớp 3

    Với các biến a,b,c,d,e,f,g,h,i là các số nằm trong khoảng 1-9 (các biến có
    thể có giá trị giống nhau), dạng biểu thức:

      a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 = 66
    """
    START = time.time()
    print(START)
    result = None
    lst = []
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                for e in range(1,10):
                    for f in range(1,10):
                        for g in range(1,10):
                            for h in range(1,10):
                                for i in range(1,10):
                                    a = 66 - (13 * b / c + d + 12 * e - f - 11 + g * h / i - 10)
                                    if (a > 0) & (a <10) & a.is_integer():
                                        # print([a,b,c,d,e,f,g,h,i])
                                        lst.append([int(a),b,c,d,e,f,g,h,i])
                                            
    result = lst            
    STOP = time.time()
    print(STOP)
    TIME = STOP - START
    
    print(TIME)
    return result
    
def main():
    print(len(solve()))


if __name__ == "__main__":
    main()
