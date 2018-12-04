# 数据清洗

本次只抓取了评论信息中的昵称(nickname)、评论日期(rate_date)、颜色(color)、大小(size)这些数据。评论信息存储如下：  

![image](https://note.youdao.com/yws/public/resource/c5d9ce15052fef3823a4328d61c255ca/xmlnote/67B4D5B77A6747CD895913F8F8DC9701/10210)  

不过数据有些不规范，项目中只对color和size两种数据进行清洗。因为在每个店铺中商品的颜色叫法可能不同，所以需要将颜色名称进行统一。如所有包含'紫'的颜色可以
认为是紫色，所有包含'粉'的颜色可以认为是粉色。   

新建立一个color1字段：  

```
mysql>alter table xz add color1 char(20);
```

将清洗后的颜色值保存到color1字段中：

```
mysql> update xz set color1='灰色' where xz_color like '%灰%';
mysql> update xz set color1='红色' where xz_color like '%红%';
mysql> update xz set color1='肤色' where xz_color like '%肤%';
mysql> update xz set color1='紫色' where xz_color like '%紫%';
mysql> update xz set color1='绿色' where xz_color like '%绿%';
mysql> update xz set color1='黑色' where xz_color like '%黑%';
mysql> update xz set color1='杏色' where xz_color like '%杏%';
mysql> update xz set color1='蓝色' where xz_color like '%蓝%';
mysql> update xz set color1='粉色' where xz_color like '%粉%';
```

新建字段size1和size2，保存罩杯的清洗数值：

```
mysql> update xz set size1='A' where xz_size like '%A';
mysql> update xz set size1='B' where xz_size like '%B';
mysql> update xz set size1='C' where xz_size like '%C';
mysql> update xz set size1='D' where xz_size like '%D';
```
```
mysql> update xz set size2='70' where xz_size like '70%';
mysql> update xz set size2='75' where xz_size like '75%';
mysql> update xz set size2='80' where xz_size like '80%';
mysql> update xz set size2='85' where xz_size like '85%';
```

清洗后的存储效果如下：

![image](https://note.youdao.com/yws/public/resource/7ee9ac8232d752b669a10ae5554e80a4/xmlnote/A365A7D63A4946DF8935DD521582B85C/10215)

# 数据可视化

使用matplotlib库绘制出商品不同尺寸及各种颜色的销售情况。

## 尺寸销量柱状图

```
plt.subplot(221)
size_df['销量'].plot(kind='bar', color=colors, yerr=40, ecolor='r', capsize=5)
plt.xticks(index, labels)
plt.yticks(np.arange(0, 1601, 200))
plt.xlabel('尺寸')
plt.ylabel('销量')
plt.title('尺寸条形图')
for x, y in enumerate(size_df['销量']):
    plt.text(x, y+45, y, ha='center', va='bottom')
```

## 尺寸销量饼图

```
rcParams['font.sans-serif'] = ['SimHei']  # 设置matplotlib图形化要显示的字体
size_data = read_sql('select size1 from xz', conn)
size_count = size_data.groupby('size1').size()
total = size_count.sum()
size_df = size_count.to_frame(name='销量')
index = np.arange(4)
colors = ['#07DB00', '#3986FF', '#E933C1', '#FF7935']
labels = ['A罩杯', 'B罩杯', 'C罩杯', 'D罩杯']
figure(figsize=(10, 8), dpi=80)

plt.subplot(222)
size_df['销量'].plot(kind='pie', labels=labels, autopct='%1.2f%%', pctdistance=0.6, labeldistance=1.2, colors=colors)
plt.legend(bbox_to_anchor=(0.8, 0.9), frameon=False)
```

## 颜色销量柱状图

```
plt.subplot(223)
color_count.plot(kind='bar', alpha=0.8)
plt.xlabel('颜色')
plt.ylabel('销量')
plt.yticks(np.arange(0, 1001, 200))
plt.title('颜色条形图')
for x, y in enumerate(color_count):
    plt.text(x, y+15, y, ha='center', va='bottom')
plt.show()
```

结果如下图：  

![image](https://note.youdao.com/yws/public/resource/7ee9ac8232d752b669a10ae5554e80a4/xmlnote/0CC406C55CB34AF687A6B38E4C6198CF/10218)
