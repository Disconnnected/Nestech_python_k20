#!/usr/bin/env python3

import csv
import os
import time
from datetime import datetime
# bài này khó. làm đc thì làm 


def find_max_price(datafile):
    f = open(datafile)
    dr = csv.DictReader(f, ["time", "price", "UNKNOWN"])  # NOQA
    # Viết tiếp code vào đây
    price = 0
    t = ""
    try:
        for i in dr:
            if float(i["price"]) > price:
                price = float(i["price"])
                t = i["time"]
        pass

    finally:
        get_date = datetime.fromtimestamp(float(t))

        price_time = datetime.date(get_date)

        result = (str(price_time),f"{price:,}")

        f.close()
    
    return  result


def solve():
    """Tìm ngày giá BTC lên cao nhất. Trả về Tuple chứa ngày ở định dạng
    YYYY-mm-dd (VD: 2017-06-19) và giá VND của 1 BTC
    """
    # http://api.bitcoincharts.com/v1/csv/
    datafile = "localbtcVND.csv"
    exdir = os.path.dirname(__file__)
    datapath = os.path.join(exdir, datafile)

    result = find_max_price(datapath)
    return result


def main():
    now = time.gmtime(int(time.time()))
    print(now.tm_year, now.tm_mon, now.tm_mday)
    print(solve())


if __name__ == "__main__":
    main()
