"""
write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
example:
 a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
"""

# def remove_dupicates_element(x,y,z):
#     #Join two list
#     z = x + y 

#     #Sort list
#     z.sort()

#     #Set items after sorting and switching to list mode
#     z = list(set(z))
    
#     return z

def dupicates_element(x,y,z):
    for i in x:
        if i in b:
            z.append(i)
    return list(set(z))
        

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

print(dupicates_element(a,b,c))
# print(remove_dupicates_element(a,b,c))