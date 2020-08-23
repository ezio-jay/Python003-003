学习笔记
# python 语法
yield 逐个返回内容
‘’‘
def get_urls():
    myurl="https://maoyan.com/films?showType=3&sortId=3"

    response = requests.get(myurl, headers = header)
    #获取网页的内容
    bs_info = bs(response.text, 'html.parser')
    #解析网页的内容
    for tags in bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'}):
        yield 'http://maoyan.com' + tags.a.get('href')
’‘’
#遇到的问题
scrapy 框架使用时忘记打开ITEM_PIPELINES