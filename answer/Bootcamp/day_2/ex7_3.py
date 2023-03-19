#!/usr/bin/env python3


__doc__ = """
Yêu cầu:
- Dùng pip cài thư viện PyYAML, import yaml và dùng `yaml.safe_load` để biến nội
dung trong file thành kiểu dữ liệu trên Python.

- In ra số phần tử của kiểu dữ liệu vừa tạo. Dùng thư viện json để
 `json.dump` nội dung, ghi ra một file tên là event.json trong thư mục hiện tại.

- Dùng thư viện pickle để pickle.dump nội dung trên ra file event.pkl trong
  thư mục hiện tại. Chú ý khi mở file, phải mở ở chế độ ghi ở dạng binary. Đọc
  thêm tại đây:
  https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files`

- In ra kích thước của mỗi file đã tạo.

Gợi ý: sử dụng os.stat(filename).st_size
Read: open multiple files https://docs.python.org/3/reference/compound_stmts.html#with
"""  # NOQA


import json  # NOQA
import os  # NOQA
import pickle  # NOQA
import yaml  # NOQA


path = 'event.yaml'

def your_function():
    """Trả về số phần tử của kiểu dữ liệu sau khi dùng module `yaml` để load

    Thực hiện các yêu cầu tại ``__doc__``

    :rtype int:
    """
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    result = None
    data = None
    
    #load file  event.yaml
    exdir = os.path.dirname(__file__)
    path_yaml = os.path.join(exdir,path)
    if os.path.exists(path_yaml):
        with open(path_yaml, 'r') as f:
            data = yaml.safe_load(f)
    else:
        print('not file')
    
    # len phan tu
    data_number = len(data)
    
    # save file json
    path_json = os.path.join(exdir,'event.json')
    with open(path_json, 'w') as f:
        json.dump(data,f)
    
    # save file pkl
    path_pkl = os.path.join(exdir,'event.json')        
    with open(path_pkl, 'wb') as f:
        pickle.dump(data,f)
        
    json_size = os.stat(path_json).st_size
    pkl_size = os.stat(path_pkl).st_size
    
    result =data_number
    
    return result


def solve():
    """không cần viết code trong hàm `solve`, chỉ thực hiện
    đổi tên lại function của mình cho phù hợp

    :rtype int:
    """
    result = your_function()

    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
