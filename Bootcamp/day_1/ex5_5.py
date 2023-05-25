# #!/usr/bin/env python3
import os


filename = "input_5_5.txt"
datafile = os.path.join(os.path.dirname(__file__), filename)
MAGIC_NUMBER = 20200000


# def solve(inputfile, N=5):
#     """
#     Đọc danh sách từ file `inputfile`.
#     https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

#     Biết những bạn có tên bắt đầu bằng chữ `D` sẽ ngồi phòng thi số N,
#     các bạn có tên bắt đầu chữ `H` ngồi phòng thi số N+1, và các bạn còn lại,
#     nếu có tên kết thúc là `ng` sẽ ngồi cùng phòng các bạn tên `H`, còn lại
#     ngồi cùng phòng `D`.
#     Tất cả các đều sinh năm 1990.
#     Mã được tính bằng: hash(NAME) % MAGIC_NUMBER
#     (chú ý số này mỗi lần chạy sẽ khác nhau).
#     Ví dụ: mã của 'Dung' là: hash('Dung') % MAGIC_NUMBER

#     Trả về result là list các tuple chứa
#     (mã sinh viên, tên học viên, năm sinh, phòng thi), sắp xếp
#     theo thứ tự tên học viên.
#     """
#     result = None


#     return result


# def main():
#     filename = datafile
#     # Cho danh sách students
#     for msv, *ignore, room in solve(filename):
#         print(msv, room)
#         print("DEBUG", ignore, type(ignore), len(ignore))


# if __name__ == "__main__":
#     main()

def read_file():
    print("Now reading the file..")
    try:
        f = open("Bootcamp\day_1\input_5_5.txt", "r")
        for line in f.readlines():
            print(line)
        f.close()
    except Exception:
        print("Could not read to file")

f = open("Bootcamp\day_1\input_5_5.txt", "r")
names = f.readlines()
names.sort()
lst_tup = []
for name in names:
    if(name[0] == "D"):
        lst_tup.append((hash(name)% MAGIC_NUMBER,name[:-1],1990,'N'))
    elif((name[0]=="H") or (name[-3:-1]=="ng")):
        lst_tup.append((hash(name)% MAGIC_NUMBER,name[:-1],1990,'N+1'))
    else:
        lst_tup.append((hash(name)% MAGIC_NUMBER,name[:-1],1990,'N'))

print('sắp xếp theo tên: ')
for i in lst_tup:
    print(i)