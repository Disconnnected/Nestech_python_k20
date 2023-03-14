"""
write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
example:
 a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
# b1: loại bỏ phần tử trùng trong list.
a_set=set(a)
b_set=set(b)
# b2: vòng lặp set1, check tồn tại trong set2 và append vào list mới  
for i in a_set:
  if i in b_set:
    c.append(i)
print(c)