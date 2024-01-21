
from bs4 import BeautifulSoup
import requests
import random
import re 
import csv
from datetime import datetime

def soup(URL):
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    sts=['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36']
    headers = {
        'User-Agent': f'{sts}',
        'From': 'youemail@salo.uz'}  
    # Загружаем страницу с отключенной проверкой SSL
    response = requests.get(URL, headers=headers, verify=False)
    # Создаем объект BeautifulSoup с использованием lxml парсера (или другого поддерживаемого парсера)
    soup = BeautifulSoup(response.content, 'lxml')
    return soup

def table(html):
    """получает весь html текст и венет лист данные"""
    div_table = html.find('div', class_='col-xs-12 table-responsive')
    trs = div_table.find('tbody').find_all('tr')
    tr_=[]
    for tr in trs:
        tds = tr.find_all('td')
        td_=[]
        for td in tds:
            td_.append(td.get_text().strip().replace(' ','').replace('\n',' '))
        tr_.append(td_)
    return tr_

def last_page(html):
    """принимает вес текст html и найдет последную строку и его вернет"""
    last_list = html.find('li', class_='last next').find('a').get('href')
    re_ = r"\d\d\d|\d\d|\d"
    match = re.search(re_, last_list).group()
    return int(match)

def links(lastpage:int):
    """занесем последную страницу по формуле и получаем все ссылке в виде листа"""
    urls = ['https://uzse.uz/trade_results/']
    for i in range(1,lastpage+1):
        urls.append(f'https://uzse.uz/trade_results?page={i}')
    return urls

def recording_csv(data:list): 
    with open(f'{str(datetime.now())}_.csv', 'a+', newline='') as file:
        # Создаем объект для записи CSV
        writer = csv.writer(file,delimiter=';')
        # Записываем данные
        for row in data:
            writer.writerow(row)


