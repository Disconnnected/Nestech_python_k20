"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old
extra: Depending on whether the number is even or odd, print out an appropriate message to the user ("your age is odd/even")
"""

import time;

fullname = "Trần Lâm" # input("Tên ủa bạn là gì?: \n")
age = 20 #int(input("Bạn bao nhiêu tuôi"))

nowYear = time.localtime(time.time()).tm_year
futureYear = (100-age)+nowYear
age_check = lambda age : "chẵn" if age%2==0 else "lẽ"

message = f"""
Chào bạn {fullname.upper()}
Số tuổi của bạn là {age_check(age)}
Năm {futureYear}, bạn sẽ tròn 100 tuổi
"""

print(message)
