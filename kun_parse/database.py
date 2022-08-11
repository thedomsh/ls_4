import psycopg2

database = psycopg2.connect(
    database= 'news_info',
    host='localhost',
    user='postgres',
    password='123456'
)

cursor = database.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS news_info(
    news_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    post_time TEXT,
    post_name TEXT,
    post_link TEXT
)
''')

database.commit()
database.close()