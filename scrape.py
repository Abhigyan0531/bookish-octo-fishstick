from bs4 import BeautifulSoup
import requests

urls = ['https://www.cnn.com,https://www.bbc.com/news,https://www.nytimes.com/,https://www.theguardian.com/international, https://www.aljazeera.com/,https://www.reuters.com/,https://www.washingtonpost.com/,https://www.wsj.com/,https://www.nbcnews.com/,https://abcnews.go.com/,https://techcrunch.com/,https://www.theverge.com/,https://www.wired.com/,https://www.cnet.com/,https://www.techradar.com/,https://www.engadget.com/,https://gizmodo.com/,https://www.zdnet.com/,https://www.tomsguide.com/,https://www.pcmag.com/,https://www.engadget.com/,https://gizmodo.com/,https://techcrunch.com/,https://www.wired.com/,https://mashable.com/,https://www.cnet.com/,https://www.digitaltrends.com/,https://www.zdnet.com/,https://www.techradar.com/,https://www.tomsguide.com/,https://www.pcgamer.com/,https://arstechnica.com/,https://www.techspot.com/,https://thenextweb.com/']
for url in urls:
    response = requests.get(url)
    html_content = response.content

soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find('title').text
paragraphs = soup.find_all('p')

print(title)
for p in paragraphs:
    print(p.text)

with open('output.txt', 'w') as f:
    f.write(title + '\n')
    for p in paragraphs:
        f.write(p.text + '\n')