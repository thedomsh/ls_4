import psycopg2

while True:
    find_news = input('Чтобы прочитать последние новости, введите "Go": ')
    if find_news.lower() == 'stop':
        break

    try:
        data = 'https://kun.uz/'.info()

        post_time = data['news-meta'][0]['span']
        post_name = data['news-meta'][0]['small-news__title']
        post_link = data['news-meta']['small-news__title'][0]['href']
        print(f"""{post_time}. {post_name}
 Подробнее: {post_link}""")

    database = psycopg2.connect(
        database='news_info',
        host='localhost',
        user='postgres',
        password='123456'
    )

    cursor = database.cursor()

    cursor.execute('''
            INSERT INTO news_info(post_time, post_name, post_link)
            VALUES (%s, %s, %s)
            ''', (post_time, post_name, post_link))
    database.commit()
    database.close()














