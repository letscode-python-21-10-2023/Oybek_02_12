from functions import *
from datetime import datetime

print(datetime.now())
URL = 'https://uzse.uz/trade_results/'

html = soup(URL)
lastpage = last_page(html)
LINKS = links(lastpage)
tables = []
header = [['Время','ISIN','Эмитент','Тип ценной бумаги','Рынок','Площадка','Торговая цена','Кол-во ЦБ']]
for link in LINKS:
    html_ = soup(link)
    tables += table(html_) 
tables = header + tables 
with open('index.txt',mode='a+',encoding='UTF-8') as file:
    file.write(str(tables))

    
recording_csv(tables)

print(datetime.now())
"""теперь нужно разработать чтобы он записывал в экселке и в сsv и в базы данных"""
"""нужно это автоматизировать и залить в бот"""







