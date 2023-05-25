"""

cho chuỗi: list_input = [1,2,3,4,5,6,7,8]

in ra chuỗi mới với mỗi phần tử của chuỗi mới là bình thương của phần tử tương ứng trong chuỗi cũ

expected_output = [1,4,9,16,25,36,49,64]

"""
import math
list_input = [1,2,3,4,5,6,7,8]
expected_output = []
i = 0
while (i < len(list_input)):
    a = math.pow(list_input[i],2)
    i = i + 1
    expected_output.append(int(a))
print(expected_output)
