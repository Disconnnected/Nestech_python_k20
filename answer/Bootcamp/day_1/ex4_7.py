#!/usr/bin/env python3


GOOD = 1
NEUTRAL = 0
BAD = -1

def last_two_digits(year):
    year = str(year)
    return int(year[-2:])

def last_one_digits(year):
    year = str(year)
    return int(year[-1])

def solve(year1, year2):
    """Trả về tuple-3 chứa tên gọi can chi của year1, year2, và giá trị số xem
    2 tuổi này có họp hay không.

    - 1 đại diện cho hợp
    - 0 đại diện cho bình thường
    - -1 đại diện cho khắc

    Các từ trong tên đề phải viết hoa các chữ cái đầu.

    Biết có 10 thiên can::

      ['giáp', 'ất', 'bính', 'đinh', 'mậu', 'kỷ', 'canh', 'tân', 'nhâm', 'quý']

    Và 12 địa chi::

      ['tý', 'sửu', 'dần', 'mão', 'thìn', 'tị', 'ngọ', 'mui', 'thân', 'dậu',
       'tuất', 'hợi']

    Tứ hành xung: theo cặp "dần-thân", "tị-hợi" khắc nhau, còn "dần-tị/dần-hợi"
    chỉ xung nhẹ (coi là bình thường) chứ không khắc.

      ["dần", "thân", "tị", "hợi"]
      ["tý", "ngọ", "mão", "dậu"]
      ["thìn", "tuất", "sửu", "mùi"]

    Tam hợp: chỉ cần trong mỗi list là đều hợp:

      ["thân", "tý", "thìn"] - Nhóm kiên trì
      ["tị", "dậu", "sửu"] - Nhóm trí thức
      ["dần", "ngọ", "tuất"] - Nhóm độc lập
      ["hợi", "mão", "mùi"] - Nhóm ngoại giao

    Năm 2017 là năm "Đinh Dậu".

    https://vansu.net/tam-hop-tu-hanh-xung.html
    """
            #    0         1       2    3       4       5       6       7       8     9
    thiencan = ['canh', 'tân', 'nhâm', 'quý', 'giáp', 'ất', 'bính', 'đinh', 'mậu', 'kỷ']

    diachi = ['tý', 'sửu', 'dần', 'mão', 'thìn', 'tị', 'ngọ', 'mui', 'thân', 'dậu', 'tuất', 'hợi']

    xung = [["dần", "thân", "tị", "hợi"],
            ["tý", "ngọ", "mão", "dậu"],
            ["thìn", "tuất", "sửu", "mùi"]]
    
    tamhop = [["thân", "tý", "thìn"],
              ["tị", "dậu", "sửu"],
              ["dần", "ngọ", "tuất"],
              ["hợi", "mão", "mùi"]]

    #Tính Can
    for i,c in enumerate(thiencan):
        if i == last_one_digits(year1):
            can_1 = c.title()
        if i == last_one_digits(year2):
            can_2 = c.title()

    #Tính Chi
    for i,c in enumerate(diachi):
        if i == last_two_digits(year1)%12:
            chi_1 = c.title()
        if i == last_two_digits(year2)%12:
            chi_2 = c.title()
        
    can_chi_1 = f"{can_1} {chi_1}"
    can_chi_2 = f"{can_2} {chi_2}"
    
    list_xung = []
    list_bth = []

    chi = [chi_1.lower(),chi_2.lower()]

    for x in range(len(xung)):
        xung_1 = xung[x][:2]
        xung_2 = xung[x][-2:]

        bth_1 = [xung[x][0],xung[x][2]]
        bth_2 = [xung[x][0],xung[x][3]]

        list_xung.append(xung_1)
        list_xung.append(xung_2)

        list_bth.append(bth_1)
        list_bth.append(bth_2)

    hopnhau = None

    for li,t in enumerate(tamhop):
        if chi_1.lower() in tamhop[li] and chi_2.lower() in tamhop[li][li-1] or chi_2.lower() in tamhop[li] and chi_1.lower() in tamhop[li][li-1]:
            hopnhau = 1
            break
           
    if hopnhau is None:
        for x in list_xung:
            if chi == x:
                hopnhau = -1
                break
            elif chi == [b for b in list_bth] or chi_1 == chi_2:
                hopnhau = 0
            else:
                hopnhau = 0

    result = (can_chi_1,can_chi_2,hopnhau)

    return result

def main():
    # 0:
    # this = 1960
    # that = 1961
    
    # 1:
    # this = 1986
    # that = 2006

    # -1
    this = 1986
    that = 2008
    
    thiscc, thatcc, isgood = solve(this, that)
    if isgood == GOOD:
        result = "hợp"
    elif isgood == BAD:
        result = "xung"
    elif isgood == NEUTRAL:
        result = "bình thường - hợp ăn hợp ngủ là được"
    else:
        raise ValueError("Bad value {}".format(isgood))
        

    print(
        "Năm {0}({1}), năm {2}({3}): {4}".format(
            this, thiscc, that, thatcc, result
        )
    )


if __name__ == "__main__":
    main()

