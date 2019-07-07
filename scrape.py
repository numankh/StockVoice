from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

article = soup.find('article')

# Obtain the latest article title
headline = article.h2.a.text

# Obtain the summary of latest article
summary = article.find('div', class_='entry-content').p.text

# Obtain video url of latest article
vid_src = article.find('iframe', class_='youtube-player')['src']
vid_id = vid_src.split('/')[4].split('?')[0]
yt_link = f'https://youtube.com/watch?v={vid_id}'

print(yt_link)
