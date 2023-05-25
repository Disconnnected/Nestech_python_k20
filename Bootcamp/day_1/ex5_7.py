#!/usr/bin/env python3


def solve(text):
    """Thực hiện biến đổi

      input: [a, abbbccccdddd, xxyyyxyyx]
      output:[a, abb3cc4dd4, xx2yy3xyy2x]

    Giải thích: Những chữ cái không lặp lại thì output giữ nguyên chữ cái đó.
    Những chữ cái liên tiếp sẽ in ra 2 lần + số lần lặp lại liên tiếp.

    Đây là một biến thể của một thuật toán nén dữ liệu có tên Run-length
    encoding (RLE).
    Không dùng groupby, hãy giải bài này.

    NOTE: bài này có thể giải dễ dàng dùng itertools.groupby
    https://pymotw.com/3/itertools/
    https://docs.python.org/3/howto/functional.html?highlight=iterator#functional-howto-iterators
    In [7]: for c, g in itertools.groupby('abbbccacdddd'):
    ...:     print("{}{}".format(c, len(list(g))), end="")
    ...:
    a1b3c2a1c1d4
    abbbccccdddd
    """
    result = None


    return result


def main():
    print(solve("abbbccccdddd"))


if __name__ == "__main__":
    main()


lst = []
chars = ''
text_new =''
text = 'baaaaabbbbbbccccckkkkkkkb'
for index, char in enumerate(text): #duyệt index và value
    if(index > 0 and index < (len(text)-1)): #xét các phần tử ngoại trừ index[0] và chữ cuối
        if(char == text[index-1]): #nếu chữ sau giống chữ trước
            chars += char #gán vào chuỗi chars
        else:
            lst.append(chars) #gán chuỗi vào list
            chars = char    #gán chuỗi mới
    elif(index == (len(text)-1)): #duyệt chữ cuối
        if(char == text[index-1]): #nếu chữ cuối giống chữ kế cuối
            chars += char   #gán vào chuỗi chars
            lst.append(chars)   #gán chuỗi chars vào list
        else: #nếu không giống
            lst.append(chars) #gán chuỗi chars vào list
            lst.append(char) #gán chữ cuối vào list
    else:
        chars += char #gán chữ cái đầu
for i in lst:
    if(len(i)==1): #nếu chuỗi chỉ có 1 chữ
        text_new+=i #gán giá trị vào text_new
    else:
        text_new+=i[:2]+str(len(i)) #lấy 2 chữ đầu + với số lần lặp
print(text_new)
