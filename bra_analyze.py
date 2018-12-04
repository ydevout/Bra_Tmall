import pymysql
import numpy as np
from pandas import *
from matplotlib.pyplot import *
import matplotlib.pyplot as plt

conn = pymysql.connect(host='localhost', user='root', password='2558', port=3306, db='underwear')
cursor = conn.cursor()
rcParams['font.sans-serif'] = ['SimHei']  # 设置matplotlib图形化要显示的字体
size_data = read_sql('select size1 from xz', conn)
color_data = read_sql('select color1 from xz', conn)
size_count = size_data.groupby('size1').size()
color_count = color_data.groupby('color1').size()
total = size_count.sum()
size_df = size_count.to_frame(name='销量')
index = np.arange(4)
colors = ['#07DB00', '#3986FF', '#E933C1', '#FF7935']
labels = ['A罩杯', 'B罩杯', 'C罩杯', 'D罩杯']
figure(figsize=(10, 8), dpi=80)

plt.subplot(221)
size_df['销量'].plot(kind='bar', color=colors, yerr=40, ecolor='r', capsize=5)
plt.xticks(index, labels)
plt.yticks(np.arange(0, 1601, 200))
plt.xlabel('尺寸')
plt.ylabel('销量')
plt.title('尺寸条形图')
for x, y in enumerate(size_df['销量']):
    plt.text(x, y+45, y, ha='center', va='bottom')

plt.subplot(222)
size_df['销量'].plot(kind='pie', labels=labels, autopct='%1.2f%%', pctdistance=0.6, labeldistance=1.2, colors=colors)
plt.legend(bbox_to_anchor=(0.8, 0.9), frameon=False)

plt.subplot(223)
color_count.plot(kind='bar', alpha=0.8)
plt.xlabel('颜色')
plt.ylabel('销量')
plt.yticks(np.arange(0, 1001, 200))
plt.title('颜色条形图')
for x, y in enumerate(color_count):
    plt.text(x, y+15, y, ha='center', va='bottom')
plt.show()
