"""
Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!
"""

# print(max(3,0,18))
a = 4
b = 3
c = 8

for i in range(3):
    if a > b:
        if a > c:
            print(a)
        elif a < c:
            print(c)
        else:
            print("2 số a và b bằng nhau")
    elif a < b:
        if b > c:
            print(b)
        elif b < c:
            print(c)
        else: 
            print("2 số a và b bằng nhau")
    else:
        print("2 số a và b bằng nhau")