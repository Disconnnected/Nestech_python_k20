#!/usr/bin/env python3

# lst = []
def your_function(iterable, N):
    # Sửa tên, set giá trị return
    result = None
    lst_tupl = []
    tupl = ()
    for index, el in enumerate(iterable):
        if(((index+1)%N==0)&(index > 0)):
            tupl += (el,)
            lst_tupl.append(tupl)
            tupl=()
        else:
            tupl += (el,)

    result = lst_tupl
    return result
    # pass

 
def solve(iterable, N):
    """Chia input_data thành các tuple chứa N phần tử (chunk a list).
    Nếu tuple cuối không đủ phần tử thì bỏ đi.
    """
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Bạn chưa làm bài này")

    # sửa thành tên function phù hợp
    result = your_function(iterable, N)

    return result


def main():
    li = ["meo", "bo", "ga", "cho", "chim", "gau", "voi"]
    print(solve(li, 2))


if __name__ == "__main__":
    main()