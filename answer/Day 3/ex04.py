"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it."

hint: use list comprehension
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
def even_elements_sort(x,y):
    for i in x:
        if i % 2 == 0:
            y.append(i)
    print(y)
print(even_elements_sort(a,b))
