# coding:utf-8
import requests
from bs4 import BeautifulSoup
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class meitu():

    def root_url(self,url):
        html = self.request(url)
        all_a = BeautifulSoup(html.text,from_encoding='utf-8').find('div',class_='lb_box').find_all('dd')
        for a in all_a:
            title = a.get_text()
            print 'start to save:',title

            href = a.find('a')['href']
            self.html(href)

    def html(self,href):
        html = self.request(href)
        max_span = BeautifulSoup(html.text,from_encoding='utf-8').find('li',class_="bottom_show").find_all('span')
        for span_ in max_span:
            span_page = span_.get_text()[-1]
            for page in range(1,int(span_page)+1):
                if page == 1:
                    page_url =href
                else:
                    page_url = href[:-6]+"_"+ str(page)+".shtml"
                self.img(page_url)

    def img(self,page_url):
        img_html = self.request(page_url)
        img_all = BeautifulSoup(img_html.text,from_encoding='utf-8').find(
            'div',class_='l_effect_img_mid').find_all('img')
        for b in img_all:
            img_url = b['src']

            self.save(img_url)


    def save(self, img_url):
        name = img_url[-9:-4]
        img = self.request(img_url)
        f = open(name + '.jpg','ab')
        f.write(img.content)
        f.close()

    def request(self,url):
        headers={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like "
                               "Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        content = requests.get(url,headers)
        return content
Meitu = meitu()
Meitu.root_url('http://pic.yesky.com/c/6_22151.shtml')
