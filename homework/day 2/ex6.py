"""

cho chuỗi: list_input = [1,2,3,4,5,6,7,8]

in ra chuỗi mới với mỗi phần tử của chuỗi mới là bình thương của phần tử tương ứng trong chuỗi cũ

expected_output = [1,4,9,16,25,36,49,64]

"""
list_input = [1,2,3,4,5,6,7,8]
for i in list_input:
   list_input[list_input.index(i)]=i**2
print(list_input)