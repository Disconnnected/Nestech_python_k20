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
    max_price = float("-inf")
    max_timestamp = ''
    
        
    try:
        for row in dr:
            if (float(row["price"]) > max_price):
                max_price = float(row["price"])
                max_timestamp = row["time"]
        
        max_date = datetime.fromtimestamp(float(max_timestamp))
        max_date = max_date.strftime("%Y-%m-%d")
        
        max_price = f"{max_price:,}"

        # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
        # raise NotImplementedError("Bạn chưa làm bài này")
    finally:
        f.close()

    return (max_date,max_price)


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
