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
    char = ""

    for i in text.split():
        if i.isdigit():
            result.append(int(i))
        else:
            char += i
    
    char = list(char.split(","))
    i = 0                           
    while i < len(char):
        if char[i].isalpha():
            del char[i]
            i = 0
        else:
            break
    print(char)

    nlist = []
 
        
                
                
             
    print(nlist)

        
    return result

def main():
    ss = "Bé lên 3 bé đi lớp 4"
    ss = "Em ơi có bao nhiêu, 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu9"
    print(solve(ss))
    # assert solve(ss) == [3, 4]


if __name__ == "__main__":
    main()
