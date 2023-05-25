import matplotlib.pyplot as plt
import pandas as pd

noi_lam = pd.read_csv('khao sat\khaosat_noilam.csv')
met_moi = pd.read_csv('khao sat\khaosat_metmoi.csv')
thoi_gian = pd.read_csv('khao sat\khaosat_thoigian.csv')
viec_lam = pd.read_csv('khao sat\khaosat_vieclam.csv')

# print(noi_lam)

gr_noi_lam = noi_lam.groupby('answer').size()
print(gr_noi_lam.plot.pie(autopct='%1.1f%%',startangle=90, explode = [0.1,0.2,0.1,0,0.2]))
plt.suptitle('Anh/chị đang làm ở đâu?')
plt.show()