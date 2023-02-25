"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it."

hint: use list comprehension
"""

def even_elements_sort(x,y):
    for i in x:
        if i % 2 == 0:
            y.append(i)
    return y 

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []

print(even_elements_sort(a,b))