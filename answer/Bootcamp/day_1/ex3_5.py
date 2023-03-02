#!/usr/bin/env python3
"""
Gợi ý: có thể dùng enumerate()
https://docs.python.org/3/library/functions.html#enumerate
"""


data = ["I", "Love", "You", "Chiu", "Chiu"]


def solve(input_data):
    """Trả về 1 `list` các `list` theo định dạng sau:

        result = [[1, "I"], [2, "Love"], [3, "You"], [4, "Chiu"], [5, "Chiu"]]

    :rtype: list
    """
    result = input_data


    #Cách 1:
    add_arr_list = []

    for i in range(len(result)):
        add_arr_list.append([i+1,result[i]])
        
    print(f"Cách 1: \n{add_arr_list}\n")

    
    #Cách 2 `Khác dấu "()" thay vì "[]" `:
    print(f"Cách 2: \n{list(enumerate(result,1))}")
    
    return result


def main():
    # xử lí in ra theo yêu cầu đề bài bên dưới
    result = solve(data)
    pass


if __name__ == "__main__":
    main()
