import os
import csv
import secrets
import time

path_dir = os.path.dirname(__file__)
path_inp = os.path.join(path_dir,'Google-Playstore.csv')
path_out = os.path.join(path_dir,'Google-Playstore-limit.csv')

count = 0
index = 0
with open(path_inp, 'r') as inp, open(path_out, 'w') as out:
    reader = csv.reader(inp)
    writer = csv.writer(out)
    # write header
    header = next(reader)
    writer.writerow(header)
    # write row
    for row in reader:
        index += 1
        if secrets.choice([False,True,False,False,False]):
            writer.writerow(row)
            time.sleep(0.001)
            count += 1
            print(f"{index} - {count}")
        if count >= 300000:
            break   