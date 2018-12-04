import re
import time
import random
import requests
import pymysql.cursors


def request_page(r_url):
    proxy_address = {'http': '121.13.71.82'}
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 '
            'Safari/537.36',
        'Connection': 'close'}
    try:
        r = requests.get(r_url, headers=headers, proxies=proxy_address)
        result = r.text
        return result
    except Exception as e:
        print('the error is: %s' % e)


def get_data():
    nickname = []
    rate_date = []
    color = []
    size = []
    # rate_content = []
    for g_url in urls:
        content = request_page(g_url)
        nickname.extend(re.findall(re.compile('"displayUserNick":"(.*?)"'), content))
        rate_date.extend(re.findall(re.compile('"rateDate":"(.*?)"'), content))
        color.extend(re.findall(re.compile('颜色分类:(.*?);'), content))  # ;
        size.extend(re.findall(re.compile('尺码:(.*?)"'), content))  # "
        # rate_content.extend(re.findall(re.compile('"rateContent":"(.*?)"'), content))
        t = random.random() * 5
        time.sleep(t)
    conn = pymysql.connect(host='localhost', port=****, user='root', passwd='2558', db='underwear', charset='utf8mb4')
    print('connection successful!')
    cur = conn.cursor()
    for n in range(0, len(nickname)):
        cur.execute("insert into xz(name, rate_data, color, size) values "
                    "('%s','%s','%s','%s')" % (nickname[n], rate_date[n], color[n], size[n]))
    conn.commit()
    print('the data insert successful!')
    cur.close()
    conn.close()


if __name__ == '__main__':
    urls = []
    for x in range(1, 70):
        # url1 = 'https://rate.tmall.com/list_detail_rate.htm?itemId={item_id}&spuId={spuid}&sellerId={sellerid}' \
        #       '&order=3&currentPage={page}'.format(item_id=544342617401, spuid=719310383, sellerid=1813097055, page=x)
        url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=544342617401&spuId=719310383&sellerId=1813097055' \
              '&order=3&currentPage={}'.format(x)
        urls.append(url)

    get_data()
