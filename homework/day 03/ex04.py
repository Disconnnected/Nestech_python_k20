"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it."

hint: use list comprehension
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

newlist = [x for x in a if x % 2 == 0]

newlist = []

for x in a:
    if x % 2 == 0:
        newlist.append(x)


