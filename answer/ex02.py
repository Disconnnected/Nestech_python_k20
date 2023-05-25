"""
write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
example:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
#lây phần tử giống nhau
if len(a)>=len(b):
  for i in range(len(a)):
      if a[i] in b and a[i] != c:
        c.append(a[i])
  print(c)
else:
  for i in range(len(b)):
      if b[i] in a and b[i] != c:
        c.append(b[i])
  print(c)

#loại bỏ phần tử trùng lặp
def remove_item(a,b,c):
  c=a+b
  c.sort()
  c = list(set(c))
  return(c)

print(remove_item(a,b,c))