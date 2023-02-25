"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

example: 
    - anna
    - civic
    - level
    - madam
    - mom
    - noon
    - radar
    - wow

<<<<<<< HEAD
"""
example = input("Mòi bạn nhập chuỗi: ")
cout=0
# print(int(len(example)))
for i in range(int(len(example)/2)):
    if example[i]==example[len(example)-i-1]:
        cout+=1
if(cout==int(len(example)/2)):
    print(f"{example} là chuỗi đối xứng")
else:
    print(f"{example} không là chuỗi đối xứng")
        
=======
"""
>>>>>>> ce1be8cee6e60a1d7368aec84d539cd6d1a7b484
