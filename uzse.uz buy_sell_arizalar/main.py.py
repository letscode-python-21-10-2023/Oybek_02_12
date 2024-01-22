from functions import *
from datetime import datetime


print(datetime.now())
URL = 'https://uzse.uz/asking_prices'
html = soup(URL)

header = [['Рынок','Площадка','Код ЦБ','Эмитент','Тип ценной бумаги','Лучшая цена продажи','Общее кол-во ЦБ на продажу','КЛучшая цена покупки','Общее кол-во ЦБ на покупку']]
tables=[]
last_page_=last_page(html)
links_=links(last_page_)
for link in links_:
    html_ = soup(link)
    tables+=table(html_)
tables = header + tables 
print(tables)
with open('index.txt',mode='w',encoding='UTF-8') as file:
    file.write(str(tables))

recording_csv(tables)
print(datetime.now())
