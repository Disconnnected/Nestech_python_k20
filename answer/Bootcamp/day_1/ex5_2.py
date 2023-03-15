#!/usr/bin/env python3
import copy
"""
Tips: dùng stdlib copy.deepcopy

In [14]: import copy

In [15]: d = [{'name': 'Dung', 'languages': ['C', 'Python']}]

In [16]: dnew = copy.deepcopy(d)

In [18]: dnew[0]['languages'].append('Elixir')

In [19]: dnew
Out[19]: [{'languages': ['C', 'Python', 'Elixir'], 'name': 'Dung'}]

In [20]: d
Out[20]: [{'languages': ['C', 'Python'], 'name': 'Dung'}]
"""


data = [
    {
        "name": "Hoang",
        "phone": "0988888888",
        "languages": [
            "Python",
            "C",
            "SQL",
            "HTML",
            "CSS",
            "JavaScript",
            "Golang",
        ],
    },
    {"name": "Duy", "girl_friend": "Maria"},
    {"name": "Dai", "girl_friend": "Angela"},
    {"name": "Tu"},
]


def solve(last_year_data):
    """
    Trả về list thông tin các học viên sau khi đã update sau 1 năm.
    Không thay đổi thông tin năm cũ.

    Biết các học viên đều học được các ngôn ngữ lập trình
    trong "languages" của "Hoang".
    Sau đó "Hoang" học thêm được ngôn ngữ "Elixir", các học
    viên khác không biết ngôn ngữ này.
    "Tu" có bạn gái tên là "Do Anh".
    "Duy" chia thay bạn gái, không còn bạn gái nữa.

    Chú ý: code tránh dựa vào thứ tự cụ thể trong để bài.
    """

    new_data = copy.deepcopy(last_year_data)

    values = []

    for i in last_year_data:
        values += list(i.values())

    languages = values[2]
    
    for i in range(len(new_data)):
        if new_data[i]["name"] != "Hoang":
            new_data[i]['languages'] = languages
        else:
            new_data[i]['languages'].append('Elixir')

        if new_data[i]['name'] == 'Tu':
            new_data[i]['girl_friend'] = 'Do Anh'
        elif new_data[i]['name'] == 'Duy':
            del new_data[i]['girl_friend']

    return new_data
    


def main():
    # Cho list chứa các dictionary chứa thông tin của các học viên:
    students = data

    # In ra màn hình tên học viên kèm tên bạn gái (nếu có)
    for i in range(len(students)):
        if 'girl_friend' in students[i]:
            print(f"Tên học viên {i+1}: {students[i]['name']}, bạn gái: {students[i]['girl_friend']}")
        else:
            print(f"Tên học viên {i+1}: {students[i]['name']}")
    
    # In ra các thông tin đã thay đổi so với năm trước của mỗi học viên.
    print("\nThông tin đã thay đổi so với năm trước:")
    print(solve(students))

if __name__ == "__main__":
    main()
