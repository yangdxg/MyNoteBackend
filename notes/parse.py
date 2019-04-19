import requests
from bs4 import BeautifulSoup


class ParseLink():

    def parse(self, link):
        headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                   "Accept-Language": "en-us",
                   "Connection": "keep-alive",
                   "Accept-Charset": "GB2312,utf-8;q=0.7,*;q=0.7"}
        if 'mp.weixin.qq.com' in link:
            # 微信文章
            response = requests.get(link, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser', from_encoding='utf-8')
            author = soup.find(id='js_name').text.strip()
            source = '微信公众号'
            title = soup.find(id='activity-name').text.strip()
            content = soup.find(id='img-content').text
            return title, author, source, response.text
        elif 'www.jianshu.com' in link:
            # 简书文章
            response = requests.get(link, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser', from_encoding='utf-8')
            title = soup.find('h1').text.strip()
            source = '简书'
            author = soup.find(class_='name').find('a').text.strip()
            content = soup.find(class_='show-content').text
            return title, author, source, content
        elif 'juejin.im' in link:
            # 掘金文章(拿不到作者名字)
            response = requests.get(link, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser', from_encoding='utf-8')
            title = soup.find('h1').text.strip()
            source = '掘金'
            author = soup.find(class_='username ellipsis').text.strip()
            content = soup.find(class_='article-content').text
            return title, author, source, content
        elif 'csdn.net' in link:
            response = requests.get(link, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser', from_encoding='utf-8')
            title = soup.find(class_='title-article').text
            author = soup.find(class_='article-info-box').find(class_='follow-nickName').text
            content = soup.find(id='content_views')
            source = 'csdn'
            return title, author, source, content
