from bs4 import BeautifulSoup
import requests
import random
import csv
import pdfkit

def last_page(soup):
    pages = soup.find('div', class_='tm-pagination__pages')
    try:
        x=int(pages.get_text().replace(' ','').strip().split()[-1])
    except:
        x=0
    return x

def soup(URL):
    sts=['ArithmeticError','mozilla','dsfdsfs','fggdfgre','lorem','opera','8080dsfdsf','werewrwerewrew','dsfq3rffewr','dsfdsfdsfew']
    headers = {
        'User-Agent': f'{sts[random.randint(0,9)]}',
        'From': 'youremail@domain.example03'}  
    response = requests.get(URL,headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

def find():
    search = input('Введи запрос сюда а я буду выгрузить: ')
    add = search.replace(' ','%20')
    URL_0 = f'https://habr.com/ru/search/?q={add}&target_type=posts&order=relevance'
    URLS = [URL_0]
    x=last_page(soup(URL_0))
    if x>=2:
        for i in range(2,x+1):
            URL = f'https://habr.com/ru/search/page{i}/?q={add}&target_type=posts&order=relevance'
            URLS.append(URL)
    return URLS


def get_info_articles(soup):
    articles = soup.find_all('article')
    data = [['id','title','link','views','read_time','author_name','create_date','author_link']]
    for article in articles:
        title = article.find('h2').get_text()
        id = article.get('id')
        link = 'https://habr.com' + article.find('h2').find('a').get('href')
        views = article.find('span', class_='tm-icon-counter__value').get_text()
        read_time = article.find('span', class_='tm-article-reading-time__label').get_text().strip()
        author_name = article.find('span', class_='tm-user-info tm-article-snippet__author').find('a',class_='tm-user-info__username').get_text().strip()
        author_link = 'https://habr.com' + article.find('span', class_='tm-user-info tm-article-snippet__author').find('a').get('href').strip()
        create_date = article.find('span', class_='tm-user-info tm-article-snippet__author').find('time').get('title')
        data.append([id,title,link,views,read_time,author_name,create_date,author_link])  
    return data
def recording_csv(data:list): 
    with open('info_articles.csv', 'a+', newline='') as file:
        # Создаем объект для записи CSV
        writer = csv.writer(file)
        # Записываем данные
        for row in data:
            writer.writerow(row)
    # print('Информации успешно записаны!')
def article_links(data):
    links = [row[2] for row in data[1:]]
    return links

def soup_article(url):
    soup_page = soup(url).find('div', class_='tm-article-presenter__content tm-article-presenter__content_narrow')
    return soup_page.prettify()

def record_html(url):
    soup_ = soup(url)
    soup_.find('div', class_='tm-page__sidebar').string = ''
    soup_.find('div', class_='tm-base-layout__header tm-base-layout__header_is-sticky').string = ''
    soup_.find('div', class_='tm-article-presenter__footer').string = ''
    soup_.find('div', class_='tm-footer-menu').string = ''
    soup_.find('div', class_='tm-footer').string = ''
    soup_.find('header', class_='tm-header').string = ''
    return str(soup_)
    

def html2pdf(soup_page,i):
    # file_name = soup_page.split('/')[-2]
    options = {
        'page-size': 'A4'
    }
    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
    pdfkit.from_string(soup_page.prettify(), f'pdfs/{i}.pdf', configuration=config, options=options)

if __name__== 'main':
    find()