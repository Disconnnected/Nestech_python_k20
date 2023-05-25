"""

cho chuỗi: list_input = [1,2,3,4,5,6,7,8]

in ra chuỗi mới với mỗi phần tử của chuỗi mới là bình thương của phần tử tương ứng trong chuỗi cũ

expected_output = [1,4,9,16,25,36,49,64]

"""

list_input = [1,2,3,4,5,6,7,8]
expected_output = []
for i in list_input:
    expected_output.append(i**2)

print(expected_output)

#  cach 2
expected_output2 = [0]*len(list_input)
i = 0
while (i < len(list_input)):
    expected_output2[i] = list_input[i]**2
    i+=1

print(expected_output2)