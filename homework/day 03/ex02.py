"""
write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
example:
 a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,8,9,4,2,4,5,6,7,8,11,23,12]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in a:
    for j in b:
        if(j==i):
            c.append(j)
c=list(set(c))
print(c)

