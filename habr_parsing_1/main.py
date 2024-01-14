from functions import *

urls_list = find()

for url_ in urls_list:
    try:
        soup_ = soup(url_)
        data = get_info_articles(soup_) #получаем данные ввиде листа
        recording_csv(data) # и записываем их в csv этот элемент объязательно должен быть на верху: data = get_info_articles(soup_)
        articles = article_links(data) # article links в листе собираем

        for article in articles:
            try:
                title = article.split('/')[-2]
                x = record_html(article)
                with open(f'htmls/{title}.html',mode='w',encoding='UTF-8') as file:
                    file.write(str(x))
            # html2pdf(x,i)

            except:
                print(title)
                continue
    except:
        continue

