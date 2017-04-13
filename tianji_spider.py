import requests
from bs4 import BeautifulSoup
headers={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like "
                               "Gecko) Chrome/22.0.1207.1 Safari/537.1"}

root_url = 'http://pic.yesky.com/c/6_20475.shtml'
html = requests.get(root_url, headers = headers)

Soup= BeautifulSoup(html.text,from_encoding='utf-8')

all_a = Soup.find('div',class_='lb_box').find_all('img')

for a in all_a:
    img_url = a['src']
    name = img_url[-9:-4]
    img = requests.get(img_url, headers=headers)
    f = open(name + '.jpg', 'ab')
    f.write(img.content)
    f.close()    title = a.get_text()
    href = a['href']
    img_html=requests.get(href,headers= headers)
    img_html_soup = BeautifulSoup(img_html.text,from_encoding='utf-8')
    img_all = img_html_soup.find('div',class_='l_effect_img_mid').find_all('img')
    for b in img_all:
        tup=b['src']
        img = requests.get(tup,headers = headers)
        name = tup[-9:-4]
        f = open(name+'.jpg','ab')
        f.write(img.content)
        f.close()