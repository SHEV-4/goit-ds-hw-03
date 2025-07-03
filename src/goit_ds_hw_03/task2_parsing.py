import requests 
from bs4 import BeautifulSoup 
import json

# Парсинг всіх цитат на сайті
def parse_quotes(url):
    data = []
    domain = "https://quotes.toscrape.com/"
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text,'html.parser')
            quotes = soup.find_all('div',class_ = 'quote')
            for quote in quotes:
                tags = quote.find('div',class_ = 'tags').find_all('a',class_ = 'tag')
                tags_for_quote = []
                for tag in tags:
                    tags_for_quote.append(tag.text)
                author = quote.find('small',class_ = 'author').text
                quote_text = quote.find('span',class_ = 'text').text
                data.append({
                    'tags':tags_for_quote,
                    'author':author,
                    'quote':quote_text
                })
            next_page = soup.find('li',class_ = 'next')
            if next_page!=None:
                url = f"{domain}{next_page.find('a')['href']}"
            else:
                break
    return data

# Отриманя всіх посилань на сторінки про авторів
def get_link_author(url):
    data = set()
    domain = "https://quotes.toscrape.com/"
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text,'html.parser')
            quotes = soup.find_all('div',class_ = 'quote')
            for quote in quotes:
                link = f"{domain}{quote.find('small',class_ = 'author').find_next_sibling('a')['href']}"
                data.add(link)
            next_page = soup.find('li',class_ = 'next')
            if next_page!=None:
                url = f"{domain}{next_page.find('a')['href']}"
            else:
                break
    array_data_link = list(data)
    return array_data_link

#Парсинг інформації про авторів
def parse_author(links):
    data = []
    for link in links:
        response = requests.get(link)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text,"html.parser")
            fullname = soup.find('h3',class_ = 'author-title').text
            born_date = soup.find('span',class_ = 'author-born-date').text
            born_location = soup.find('span',class_ = 'author-born-location').text
            description = soup.find('div',class_ = 'author-description').text
            data.append({
                "fullname":fullname,
                "born_date":born_date,
                "born_location":born_location,
                "description":description
            })
    return data

if __name__ == "__main__":
    url = "https://quotes.toscrape.com/"
    data_quotes = parse_quotes(url)
    with open('quote.json','w',encoding="utf-8") as file:
        json.dump(data_quotes,file)
    links_to_authors = get_link_author(url)
    data_authors = parse_author(links_to_authors)
    with open('authors.json','w',encoding="utf-8") as file:
        json.dump(data_authors,file)
