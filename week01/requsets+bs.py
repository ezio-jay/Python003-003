# 利用requests +BeautfulSoup库爬取猫眼电影评分前十电影
import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {"user-agent":user_agent}

#获取电影详情链接
def get_urls():
    myurl="https://maoyan.com/films?showType=3&sortId=3"

    response = requests.get(myurl, headers = header)
    #获取网页的内容
    bs_info = bs(response.text, 'html.parser')
    #解析网页的内容

    for tags in bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'}):
        yield 'http://maoyan.com' + tags.a.get('href')

urls = get_urls()

urls_top10 = [next(urls) for i in range(10)]
#获取前10个电影的链接

def get_details(url):
    
    response = requests.get(url, headers = header)
    #获取网页的内容
    bs_info = bs(response.text, 'html.parser')
    #解析网页的内容

    tags = bs_info.find('div', attrs={'class' : 'movie-brief-container'})
    
    movie_name = tags.find('h1').text
    #获取电影名字
    movie_type = ''
    
    for atags in tags.find_all('a'):
        movie_type = movie_type + ' '+ atags.text
    #获取电影类型
    movie_time = list(tags.find_all('li'))[2].text
    #获取电影上映时间
    return [movie_name, movie_type, movie_time]

top10_list = []
sleep(10)
for url in urls_top10:
    top10_list.append(get_details(url))
    sleep(5)

movie1 = pd.DataFrame(data = top10_list)

movie1.to_csv('./movie1.csv', encoding='utf8', index=False, header=False)
