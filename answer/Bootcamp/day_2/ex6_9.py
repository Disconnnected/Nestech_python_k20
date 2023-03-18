"""
Kết hợp bài 6_6 và 6_8, truy cập vào trang ketqua.net, lấy kết quả
giải đặc biệt rồi gửi tới email của chính bạn.

Trên Ubuntu/Mac, gõ lệnh crontab -e
rồi thêm dòng sau để chạy code này lúc 18h35 hàng ngày nếu máy tính đang bật.

35 18 * * * python3 /home/hvn/me/pyfml/exercises/ex6_9.py

Thay đường dẫn trên bằng đường dẫn thật trên máy bạn.
"""

import urllib.request
from ex6_8 import send_gmail

# bài này khó. cx chưa cần làm


def main():
    # Không dùng trực tiếp được do ketqua.net chặn Python
    # f = urllib.request.urlopen("https://ketqua.net")

    # Đổi User-Agent header để đóng giả làm trình duyệt Firefox
    req = urllib.request.Request(
        url="https://xoso.com.vn",
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"  # noqa
        },
    )
    with urllib.request.urlopen(req) as f:
        content = f.read().decode()
    
    # lấy danh sách giải đặc biệt
    special_prize = []
    date = ""
    for line in content.splitlines():
        if "ĐB" in line:
            # prize
            prize =[]
            search_prize = 'class="xs_prize1 prize_db">'
            indexes_prize = [index+len(search_prize) for index in range(len(line))
                        if line.startswith(search_prize, index)]
            for index in indexes_prize:
                prize.append(line[index:index+6])
            
            # name
            search_name_position = 'class=prize-col'
            indexes_name_position = [index+len(search_name_position) for index in range(len(line))
                        if line.startswith(search_name_position, index)]
            
            name = []
            for index in indexes_name_position:
                start = line.find(".html>", index)
                end = line.find("</a>", index)
                name.append(line[start+len(".html>"):end])
            
            special_prize = list(zip(name,prize))
        
            # date
            search_date_position = '<div class=header-time>'
            indexes_date_position = line.find(search_date_position)
            indexes_date_start = line.find("ngày ",indexes_date_position)
            indexes_date_end = line.find("</div><a",indexes_date_position)
            date = line[indexes_date_start+len("ngày "):indexes_date_end]
            break
    
    # print(special_prize)
    # print(date)

    ds_prize = ''
    for row in special_prize:
        ds_prize += f'{row[0]:<12}{row[1]:>10}\n'
    subject = "Kết quả xổ số ngày {}".format(date)
    content = "Giải đặc biệt ngày {} là: \n{}".format(date, ds_prize)
    YOUREMAIL = "hayashibutler@gmail.com"
    YOUREMAIL2= ["lam.tranledien@gmail.com"]
    
    print(content)
    send_gmail(YOUREMAIL, YOUREMAIL2, subject=subject, content=content)


if __name__ == "__main__":
    main()
