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

input_text = "Aquafina - Vị ngon của sự tinh khiết"

print(input_text.replace("a","@").replace("o","0").replace("s","$").replace("i","1"))
# print(input_text.replace("o","0"))
# print(input_text.replace("s","$"))
# print(input_text.replace("i","1"))