"""

cho chuỗi: list_input = [1,2,3,4,5,6,7,8]

in ra chuỗi mới với mỗi phần tử của chuỗi mới là bình Phương của phần tử tương ứng trong chuỗi cũ

expected_output = [1,4,9,16,25,36,49,64]

"""

list_input = [1,2,3,4,5,6,7,8]

expected_list = []

for i in list_input:
    i = i ** 2
    expected_list.append(i)


print(expected_list)