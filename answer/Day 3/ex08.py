"""
Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!
"""
def maximum(x,y,z):
    max = 0
    variable = ''
    if x>y and x>z:
        max = x
        variable = 'x ='
    elif y>x and y>z:
        max = y
        variable = 'y ='
    else:
        max = z
        variable = 'z ='
    return f"the largest of the three is: {variable} {max}"


def main(a,b,c):
    while True:
        try:
            a = int(a)
            b = int(b)
            c = int(c)
            return maximum(a,b,c)
        except ValueError:
            print(f"Please input Interger only: ")
            a = input("x = ")
            b = input("y = ")
            c = input("z = ")

a = input("x = ")
b = input("y = ")
c = input("z = ")
print(main(a,b,c))
