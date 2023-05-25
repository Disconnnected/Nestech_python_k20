#!/usr/bin/env python3
import string
import unidecode

def solve(text):
    """Bóc tách từ `text` ra một list các số theo thứ tự chúng xuất hiện.

    VD: 'Em ơi có bao nhiêu, 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu'
    -> [60, 20, 0]

    NOTE: không dùng `re` library
    """

    # use isalnum()

    result = []

    newt = unidecode.unidecode(text)
    
    for i,j in enumerate(newt):
        if j.isdigit() and newt[i-1].isdigit():
            result[-1] = int(newt[i-1]+j)
        elif j.isdigit():
            result.append(int(j))
    return result

    

def main():
    ss = "Bé lên 3 bé đi lớp 4"
    ss = "Em ơi có bao nhiêu, 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu9"
    print(solve(ss))
    # assert solve(ss) == [3, 4]


if __name__ == "__main__":
    main()
