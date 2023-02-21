"""
cho 1 chuỗi có sẵn, in ra màn hình chuỗi trong đó các ký tự đc yêu cầu sẽ được thay thế cho các ký tự có sẵn

đề bài: 
    - chuỗi đã cho: "Aquafina - Vị ngon của sự tinh khiết"
    - Yêu cầu: 
        - ký tự "a" đổi thành "@"
        - Ký tự "o" đổi thành "0"
        - Ký tự "s" đổi thành "$"
        - Ký tự "i" đổi thành "1"

"""

stringtext = "Aquafina - Vị ngon của sự tinh khiết"
stringtext = stringtext.replace('a','@')
stringtext = stringtext.replace('o','0')
stringtext = stringtext.replace('s','$')
stringtext = stringtext.replace('i','1')
print(stringtext)
